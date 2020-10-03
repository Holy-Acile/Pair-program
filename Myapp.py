#all okk

import re
from fractions import Fraction
import sys
from gen_problem import gen_problem_list

def cal_problem_list(problem_list):
 answer_list=[]
 for problem in problem_list:
  cal_re=cal_problem(problem)
  answer_list.append(cal_re)

 return answer_list

 # 计算单个题目
def cal_problem(input_pro):
 t1 = "'"  # 先处理假分数
 if (t1 in input_pro):
  input_pro = re.sub(r"(\d+'\d+/\d+)", r'(\1)', input_pro)
  input_pro = input_pro.replace("'", '+')

 input_pro = re.sub(r'(\d+/\d+)', r'(\1)', input_pro)  # 将再将分数优先处理

 t2 = "÷"
 if (t2 in input_pro):
  input_pro = input_pro.replace("÷", '/')

 t3 = "×"
 if (t3 in input_pro):
  input_pro = input_pro.replace("×", '*')

 transformed_pro = re.sub(r'(\d+)', r'Fraction("\1")', input_pro)  # 小数转分数


 res_int = int(eval(input_pro))
 res_fra = eval(transformed_pro) - res_int
 if (res_fra != 0 and res_int != 0):
  res = str(res_int) + "'" + str(res_fra)  # 返回分数
 else:
  res = str(eval(transformed_pro))  # 返回整数字符化

 return res  # 返回一个字符串形式的参数可能为整数，可能为真分数

 # 主动抛出异常
def raise_ex(s1,s2):
 if(s1=='-n' and s2=='-r'):
  return True
 ex = Exception('Error:参数格式错误！')
 raise ex

def main():
 try:
  s1, n, s2, r = sys.argv[1:5]
 except BaseException:
  print("Error: 输入命令错误 \n正确格式为-n num -r num \n")
 else:
  try:
   print(raise_ex(s1,s2))
  except Exception as re:
   print(re)
  else:
   try:
    int(n)
    int(r)
   except ValueError:
    print("Error:num处输入的不是整数！")
   else:

    Exer=open('Exercises' + '.txt', "w")##创建两个txt文件
    Answ=open('Answers' + '.txt', "w")

    n=int(n)
    r=int(r)
    problem = gen_problem_list(n, r)
    print(problem)
    answer=cal_problem_list(problem)

    for i in range(len(problem)):
     p = str(problem[i])
     p = str(i + 1) + '.  ' + p+' ='+ '\n'
     Exer.write(p)
    Exer.close()

    for j in range(len(answer)):
     s = str(answer[j])
     s =str(j+1)+'.  '+s+ '\n'
     Answ.write(s)
    Answ.close()
    print(answer)


if __name__ == '__main__':
 main()