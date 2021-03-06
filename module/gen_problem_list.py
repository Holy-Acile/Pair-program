from module.gen_problem import gen_problem
from module.check_problem import check_problem
from fractions import Fraction

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
