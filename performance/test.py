from fractions import Fraction
import random


#生成自然数/真分数
def gen_num(mod):
    if mod <= 0: return Fraction(0, 1)
    bit = random.randint(1, 10)

    #自然数
    if bit >= 1 and bit <= 5:
        return Fraction(random.randint(0, mod - 1), 1)
    #小于1的真分数
    elif (bit >= 6 and bit <= 8) or mod == 1:
        down = random.randint(2, mod + 5)
        up = random.randint(1, down - 1)
        return Fraction(up, down)
    #带分数
    else:
        down = random.randint(2, mod + 5)
        up = random.randint(down, mod * down - 1)
        return Fraction(up, down)


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


const_frac = Fraction(0, 1)

#检查题目是否重复
def check_problem(problem, vis):
    if str(problem) in vis: return False
    const_op = ("+", "-", "×", "÷")

    op = []
    cnt_op = 0
    for it in problem:
        if type(it) != type(const_frac) :
            if it != "(" and it != ")" :
                cnt_op += 1
                op.append(it)

    #1个运算符
    if cnt_op == 1:
        if op[0] == "-" or op[0] == "÷": 
            vis[str(problem)] = True
            return True
        tmp = problem
        tmp[0], tmp[2] = tmp[2], tmp[0]

        if str(tmp) in vis:
            return False
        else:
            vis[str(tmp)] = True
            vis[str(problem)] = True
            return True
    #2个运算符
    elif cnt_op == 2:
        if op[0] == "-" or op[0] == "÷":
            if op[1] == "-" or op[1] == "÷":
                vis[str(problem)] = True
                return True

        pos = -1
        for i in range(len(problem)):
            if problem[i] == "(": pos = i

        #交换
        if problem[pos + 2] == "+" or problem[pos + 2] == "×":
            if problem[pos + 1] > problem[pos + 3]:
                problem[pos + 1], problem[pos + 3] = problem[pos + 3], \
                                                     problem[pos + 1]

        tmp = ["("] + \
              [problem[pos + 1]] + \
              [problem[pos + 2]] + \
              [problem[pos + 3]] + [")"]

        #得到另一个运算符和运算数
        sc_op = ""
        sc_num = 0

        for i in range(0, max(0, pos)):
            if sc_op != "" and sc_num != 0: break
            if problem[i] in const_op: sc_op = problem[i]
            else: sc_num = problem[i]

        for i in range(len(problem)):
            if problem[i] == ")": pos = i

        if pos == -1: pos = 2

        for i in range(pos + 1, len(problem)):
            if sc_op != "" and sc_num != 0: break
            if problem[i] in const_op: sc_op = problem[i]
            else: sc_num = problem[i]

        #合并到tmp
        tmp = tmp + [sc_op] + [sc_num]

        if str(tmp) in vis:
            return False
        else:
            vis[str(tmp)] = True
            vis[str(problem)] = True
            return True
    #3个运算符
    else:
        vis[str(problem)] = True
        return True

const_frac = Fraction(0, 1)


#生成题目集
def gen_problem_list(cnt, mod):
    problem_list = []
    vis = {}  #记录已经存在的problem
    const_op = ("+", "-", "×", "÷")

    while cnt:
        problem = []
        while True:
            problem = gen_problem(int(mod))
            if check_problem(problem, vis): break

        vis[str(problem)] = True

        s = ""
        for it in problem:
            if type(it) != type(const_frac):  #符号
                if it == "(" or it == ")": s += it
                else: s += " " + it + " "
            else:  #数字
                pre = int(it)
                frac = it - pre
                if frac == 0:
                    s += str(pre)
                elif pre == 0:
                    s += str(frac)
                else:
                    s += str(pre) + "'" + str(frac)

        problem_list.append(s)
        cnt -= 1

    return problem_list


if __name__ == "__main__":
    cnt = 10000
    mod = 10
    problem_list = gen_problem_list(cnt, mod)