from module.gen_problem import gen_problem
from module.check_problem import check_problem


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
            if it in (const_op + ("(", ")")):  #符号
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
    problem_list = gen_problem_list(5, 10)
    print(problem_list)

    vis = {}
    for problem in problem_list:
        if str(problem) in vis:
            print("Error!!!")
        else:
            vis[str(problem)] = True

    print("Finish test!!!")
