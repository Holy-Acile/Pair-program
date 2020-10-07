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
                    if part_num.denominator > mod + 5 :
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

    return problem
