import sys
sys.path.append("../../../")
from module.cal_problem import cal_problem

if __name__ == "__main__":
    pro = "8'2/7 + (5'11/12 + 7'1/2)"
    stand_ans="21'59/84"
    answer = cal_problem(pro)
    if answer==stand_ans:
        print("Finish test!!!")
    else:
        print("Error!!!")