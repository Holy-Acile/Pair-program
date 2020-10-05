import sys
sys.path.append("../../../")
from module.gen_problem_list import gen_problem_list

if __name__ == "__main__":
    cnt = 10
    mod = 10
    problem_list = gen_problem_list(cnt, mod)
    print(problem_list)