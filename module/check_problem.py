#检查题目是否重复
def check_problem(problem, vis):
    if str(problem) in vis: return False
    const_op = ("+", "-", "×", "÷")

    op = []
    cnt_op = 0
    for it in problem:
        if it in const_op:
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