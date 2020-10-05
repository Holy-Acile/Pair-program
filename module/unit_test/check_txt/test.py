import sys
sys.path.append("../../../")
from module.check_txt import check

if __name__ == "__main__":
    pro_list = ["8'2/7 + (5'11/12 + 7'1/2)","1/10 × 9 - 0 + 9'3/10","2/3 ÷ (7 + (4 × 7/8))"]
    user_ans=["21'59/84","21'59/84","21'59/84"]
    stand_ans='Correct: '+ str(1) + ' ('  +str(1)+ ')'+'\n'+'Wrong: ' + str(2) + ' (' + "2, 3"+ ')'
    answer = check(pro_list,user_ans)

    if answer==stand_ans:
        print("Finish check test!!!")
    else:
        print("Error!!!")