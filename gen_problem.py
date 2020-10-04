from fractions import Fraction
import random

#生成自然数/真分数
def gen_num(mod):
    if mod <= 0 : return Fraction(0, 1)
    bit = random.randint(1, 10)

    if bit >= 1 and bit <= 5:                    #自然数
        return Fraction(random.randint(0, mod-1), 1)
    elif (bit >= 6 and bit <= 8) or mod == 1 :   #普通真分数
        down = random.randint(2, mod+5)
        up = random.randint(1, down-1)
        return Fraction(up, down)
    else :                                       #带分数
        pre = random.randint(1, mod-1)
        down = random.randint(2, mod+5)
        up = random.randint(1, down-1)
        return pre + Fraction(up, down)

#生成题目
def gen_problem(mod):
    problem = []
    const_op = ("+", "-", "×", "÷")

    #生成运算符
    cnt_op = random.randint(1, 3)
    op_list = []
    while cnt_op :
        bit = random.randint(0, 3)
        op_list.append(const_op[bit])
        cnt_op -= 1

    num = gen_num(mod)
    problem.append(num)
    last_op = " "
    for op in op_list :
        part_num = gen_num(mod)

        swap_flag = random.randint(0, 1)

        #进行一次运算
        t = 0
        if op == "+" :
            t = num + part_num
        elif op == "-" :
            if swap_flag == 0 or num >= mod:
                swap_flag = 0
                t = num - part_num
                while t < 0 :
                    part_num = gen_num(min(mod, int(t)))
                    t = num - part_num
            else :
                t = part_num - num
                while t < 0 :
                    part_num = gen_num(int(mod-num)) + num
                    t = part_num - num
        elif op == "×" :
            t = num * part_num
        else : 
            if swap_flag == 0 :
                while part_num == 0 : part_num = gen_num(mod)
                t = num / part_num
            else :
                if num == 0 :
                    swap_flag = 0
                    while part_num == 0 : part_num = gen_num(mod)
                    t = num / part_num
                else :
                    t = part_num / num
        
        #加括号
        bracket_flag = False
        if op == "×" or op == "÷" :
            if last_op == "+" or last_op == "-" :
                bracket_flag = True

        if bracket_flag :
            problem = ["("] + problem + [")"]

        #交换位置
        if swap_flag == 1 :
            if bracket_flag == False and last_op != " ":
                problem = ["("] + problem + [")"]
            problem = [part_num] + [op] + problem
        else :
            problem = problem + [op] + [part_num]
        
        num = t
        last_op = op

    return problem

def check_problem(problem, vis) :
    if str(problem) in vis : return False
    const_op = ("+", "-", "×", "÷")

    op = []
    cnt_op = 0
    for it in problem :
        if it in const_op :
            cnt_op += 1
            op.append(it)

    if cnt_op == 1 :
        if op[0] == "-" or op[0] == "÷" : return True
        tmp = problem
        tmp[0], tmp[2] = tmp[2], tmp[0]

        if str(tmp) in vis : 
            return False
        else : 
            vis[str(tmp)] = True
            return True

    elif cnt_op == 2 :
        if op[0] == "-" or op[0] == "÷" :
            if op[1] == "-" or op[1] == "÷" :
                return True
        
        pos = -1
        for i in range(len(problem)) :
            if problem[i] == "(" : pos = i
        
        #交换
        if problem[pos+2] == "+" or problem[pos+2] == "×" :
            if problem[pos+1] > problem[pos+3] :
                problem[pos+1], problem[pos+3] = problem[pos+3], problem[pos+1]
        
        tmp = ["("] + [problem[pos+1]] + [problem[pos+2]] + [problem[pos+3]] + [")"]

        #得到另一个运算符和运算数
        sc_op = ""
        sc_num = 0

        for i in range(0, min(0, pos)) :
            if sc_op != "" and sc_num != 0 : return True
            if problem[i] in const_op : sc_op = problem[i]
            else : sc_num = problem[i]
        
        for i in range(len(problem)) :
            if problem[i] == ")" : pos = i
        
        if pos == -1 : pos = 2
        
        for i in range(pos+1, len(problem)) :
            if sc_op != "" and sc_num != 0 : return True
            if problem[i] in const_op : sc_op = problem[i]
            else : sc_num = problem[i]
        
        #合并到tmp
        tmp = tmp + [sc_op] + [sc_num]

        if str(tmp) in vis : 
            return False
        else :
            vis[str(tmp)] = True
            return True

    else : 
        return True

def gen_problem_list(cnt, mod):
    problem_list = []
    vis = {}
    const_op = ("+", "-", "×", "÷")

    while cnt :
        problem = []
        while True :
            problem = gen_problem(int(mod))
            if check_problem(problem, vis) : break
        
        vis[str(problem)] = True

        s = ""
        for it in problem :
            if it in (const_op + ("(", ")") ) :  #符号
                if it == "(" or it == ")" : s += it
                else : s += " " + it + " "
            else :               #数字
                pre = int(it)
                frac = it - pre
                if frac == 0 :
                    s += str(pre)
                elif pre == 0 :
                    s += str(frac)
                else :
                    s += str(pre) + "'" + str(frac)

        problem_list.append(s)
        cnt -= 1
    
    return problem_list

if __name__ == "__main__" :
    problem_list = gen_problem_list(5, 10)
    print(problem_list)

    vis = {}
    for problem in problem_list :
        if str(problem) in vis :
            print("Error!!!")
        else :
            vis[str(problem)] = True

    print("Finish test!!!")
