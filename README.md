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

大部分模块基本都可以用随机生成数据的方法，利用代码检测是否符合约束条件。这里说一下需要自己构造样例来验证正确性的模块：判定两个问题是否重复：check_problem.py

### check_problem模块思路

当时设计这个模块时，是这样想的：运算符数量小于3的问题，通过有限次交换+和×左右，重复的概率有点大。但是运算符等于3的时候，如果不是一模一样的问题，基本上通过交换重复的概率很小。所以，这个模块的检查思路是：

1. 首先直接判断这个问题没交换前，之前是否出现过。出现则返回，未出现则下一步
2. 如果是这个问题有3个运算符，直接返回
3. 如果这个问题有1个运算符，那么交换运算符左右的数，看这个交换后的问题是否出现过。
4. 如果这个问题有2个运算符，统一把问题转化成这样的格式（表达式意义要相同）：`(num1 + op1 + num2) + op2 num3`。如果`op1`是加号或者乘号，要保证`num1`小于等于`num2`；如果不能转化为上述格式，说明一定不重复，返回即可。转化为这样的格式后，看这个格式的问题之前是否出现过。

### 测试模块代码

```python
import sys
sys.path.append("../../../")
from module.check_problem import check_problem

if __name__ == "__main__":
    test = [
        [   [5, "+", 4], [4, "+", 5], ["same"] ],
        [   [5, "+", 4], [5, "+", 5], ["diff"] ],
        [   [1, "×", 2], [2, "×", 1], ["same"] ],
        [   [5, "-", 5], [5, "-", 5], ["same"] ],
        [   [5, "÷", 1], [1, "÷", 5], ["diff"] ],
        [   [1, "+", 2, "-", 3], [2, "+", 1, "-", 3], ["same"] ],
        [   [1, "+", 2, "+", 3], [1, "+", 3, "+", 2], ["diff"] ], 
        [   [1, "+", 2, "+", 3], [3, "+", "(", 1, "+", 2, ")"], ["same"] ],
        [   [1, "+", 2, "+", 3], [3, "+", "(", 2, "+", 1, ")"], ["same"] ],
        [   [1, "+", "(", 2, "×", 3, ")"], [2, "×", 3, "+", 1], ["same"] ],
        []
    ]

    flag = True

    for problem_list in test :
        if len(problem_list) == 0 : break

        vis = {}
        ok = True

        for problem in problem_list :
            if len(problem) == 1 : break
            ok = check_problem(problem, vis)
            if ok == False : break

        if ok :
            if problem_list.pop() != ["diff"] :
                print("Error!!!")
                print(problem_list)
                flag = False
        else :
            if problem_list.pop() != ["same"] :
                print("Error!!!")
                print(problem_list)
                flag = False
    
    if flag :
        print("Finish test!!!")
```

### 样例设计思路

样例：

1. $5 + 4, 4 + 5\ (same)$
2. $5 + 4, 5 + 5\ (different)$
3. $1 × 2, 2 × 1\ (same)$
4. $5 - 5, 5 - 5\ (same)$
5. $5 ÷ 1, 1 ÷ 5\ (different)$
6. $1 + 2 - 3, 2 + 1 - 3\ (same)$
7. $1 + 2 + 3, 1 + 3 + 2\ (different)$
8. $1 + 2 + 3, 3 + (1 + 2)\ (same)$
9. $1 + 2 + 3, 3 + (2 + 1)\ (same)$
10. $1 + (2 × 3), 2 × 3 + 1\ (same)$

思路：

1. 前5个样例是针对一个运算符，后5个样例针对两个运算符
2. 1-3个样例，来判断普通的交换是否正确
3. 第4个样例，来判断是否能够判定重复问题
4. 第5个样例，来判断不能交换的情况
5. 第6个样例，来判断普通的交换是否正确
6. 第7个样例，来判断优先级问题（运算符优先级相同情况下，从左到右结合）
7. 第8个样例，在第7个样例基础上，还要判断整体交换
8. 第9个样例，在第8个样例基础上，还要判断括号内部交换
10. 第10个样例，验证乘法是否能正确判断


## 效能分析



## 项目小结