import sys
sys.path.append("../../../")
from module.cal_problem_list import cal_problem_list

if __name__ == "__main__":
    pro_list = ["8'2/7 + (5'11/12 + 7'1/2)","1/10 × 9 - 0 + 9'3/10","2/3 ÷ (7 + (4 × 7/8))"]
    stand_ans=["21'59/84","10'1/5","4/63"]
    answer = cal_problem_list(pro_list)
    if answer==stand_ans:
        print("Finish cal_problem_list test!!!")
    else:
        print("Error!!!")
