# 结对项目

| 软件工程 | [点我](https://edu.cnblogs.com/campus/gdgy/informationsecurity1812/) |
| :-----------------: | :---------------: |
| 作业要求 | [点我](https://edu.cnblogs.com/campus/gdgy/informationsecurity1812/homework/11157) |
| 作业目标 | 熟悉如何结对开发项目 |

## Github

开发者（学号）：
- 王欢：
- 孔止：3118005414

Github链接：
[https://github.com/Holy-Acile/Pair-program](https://github.com/Holy-Acile/Pair-program)

Github目录结构：
```txt
document    #设计文档
|-- 需求分析文档.md
|-- 模块设计文档.md

module      #模块
|-- unit_test       #模块单元测试
|-- *.py            #模块代码

performance #性能分析
|-- before          #改进前
    |-- *.txt           #line_profiler性能分析
    |-- *.png           #实际运行时间
|-- after           #改进后
|-- test.py         #测试代码

Myapp.py            #主程序
Exercises.txt       #生成的题目
Answers.txt         #题目的答案
```

## PSP

| PSP2.1 | Personal Software Process Stages | 预估耗时<br>（分钟） | 实际耗时<br>（分钟） |
| :-- | :-- | -- | -- |
| Planning | 计划 |  |  |
 | · Estimate | · 估计这个任务需要多少时间 |  |  |
| Development | 开发 |  |  |
 | · Analysis | · 需求分析 (包括学习新技术) |  |  |
 | · Design Spec | · 生成设计文档 |  |  |
 | · Design Review | · 设计复审 |  |  |
 | · Coding Standard | · 代码规范 (为目前的开发制定合适的规范) |  |  |
 | · Design | · 具体设计 |  |  |
 | · Coding | · 具体编码 |  |  |
 | · Code Review | · 代码复审 |  |  |
 | · Test | · 测试 (自我测试，修改代码，提交修改) |  |  |
| Reporting | 报告 |  | |
 | · Test Repor | · 测试报告 |  |  |
 | · Size Measurement | · 计算工作量 |  |  |
 | · Postmortem & Process Improvement Plan | · 事后总结, 并提出过程改进计划 |  |  |
| | · 合计 |  |  |

## 设计实现过程



## 代码说明

关键性代码，生成问题：gen_problem.py

### 代码

```python
from module.gen_num import gen_num
import random


#生成题目
def gen_problem(mod):
    problem = []
    const_op = ("+", "-", "×", "÷")

    ok = False
    while ok == False :
        ok = True

        #生成运算符
        cnt_op = random.randint(1, 3)
        op_list = []
        while cnt_op:
            bit = random.randint(0, 3)
            op_list.append(const_op[bit])
            cnt_op -= 1

        num = gen_num(mod)
        problem = [num]
        last_op = " "
        for op in op_list:
            part_num = gen_num(mod)

            #交换标记，决定problem(值为num)和part_num的位置
            swap_flag = random.randint(0, 1)

            t = 0  #num和part_num的运算结果
            #加
            if op == "+":
                t = num + part_num
            #减
            elif op == "-":
                #对problem和part_num的位置进行分类
                if swap_flag == 0 or num >= mod:
                    swap_flag = 0
                    t = num - part_num
                    while t < 0:
                        part_num = gen_num(min(mod, int(num)))
                        t = num - part_num
                else:
                    t = part_num - num
                    while t < 0:
                        part_num = gen_num(int(mod - num)) + num
                        t = part_num - num
                    if mod > 5 and part_num.denominator > mod :
                        ok = False
                        break
            #乘
            elif op == "×":
                t = num * part_num
            #除
            else:
                #对problem和part_num的位置进行分类
                if swap_flag == 0:
                    while part_num == 0:
                        part_num = gen_num(mod)
                    t = num / part_num
                else:
                    if num == 0:
                        swap_flag = 0
                        while part_num == 0:
                            part_num = gen_num(mod)
                        t = num / part_num
                    else:
                        t = part_num / num

            #加括号
            bracket_flag = False
            if op == "×" or op == "÷":
                if last_op == "+" or last_op == "-":
                    bracket_flag = True

            if bracket_flag:
                problem = ["("] + problem + [")"]

            #交换位置
            if swap_flag == 1:
                if bracket_flag == False and last_op != " ":
                    problem = ["("] + problem + [")"]
                problem = [part_num] + [op] + problem
            else:
                problem = problem + [op] + [part_num]

            num = t
            last_op = op
        
        if mod <= 5 and num == 0 : ok = False

    return problem
```

### 思路

因为一个问题，其实就是一个算术表达式。所以，我们只要构造出符合条件的算术表达式就可以了。这里采用了**增量构造表达式**的方法，方法如下：

1. 假设当前的表达式为`problem`
2. 这时，随机生成一个数`part_num`，和一个操作符`op`
3. 接着，我们可以由此生成新的表达式，这个表达式为：`(problem) + op + part_num`，或者：`part_num + op + (problem)`
4. 新的表达式又可以作为`problem`，执行第2步

代码整体思路：

1. 预处理出要生成什么运算符
2. 初始化表达式`problem`，设置变量`num`。`num`的含义为：表达式`problem`的值
3. 进入增量构造表达式的循环
4. 生成`part_num`
5. 设置标记变量`swap_flag`，作用：决定`problem`和`part_num`的相对位置
6. 根据`num`，`part_num`和`swap_flag`计算出目标表达式的值
7. 设置标记变量`bracket_flag`，作用：决定`problem`是否有必要加括号
8. 根据标记变量，`part_num`和运算符`op`，生成目标表达式，然后再赋值给`problem`

## 测试说明



## 效能分析



## 项目小结