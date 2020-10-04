from module.cal_problem import cal_problem


#计算题目集
def cal_problem_list(problem_list):
    answer_list = []
    for problem in problem_list:
        cal_re = cal_problem(problem)
        answer_list.append(cal_re)
    return answer_list
