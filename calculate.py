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

def cal_problem(input_pro):
 '''
 1.真分数包含‘的要替换为加号
 2.分数要用小括号括起来
 3.乘号除号替换
 '''

 t1 = "'" #先处理假分数
 if (t1 in input_pro):
  input_pro = re.sub(r"(\d+'\d+/\d+)", r'(\1)', input_pro)
  input_pro = input_pro.replace("'", '+')

 input_pro = re.sub(r'(\d+/\d+)', r'(\1)', input_pro)  #将再将分数优先处理


 t2 = "÷"
 if (t2 in input_pro):
  input_pro = input_pro.replace("÷", '/')

 t3 = "×"
 if (t3 in input_pro):
  input_pro = input_pro.replace("×", '*')


 transformed_pro = re.sub(r'(\d+)', r'Fraction("\1")', input_pro)  # 小数转分数
 print(transformed_pro)

 res_int = int(eval(input_pro))
 res_fra = eval(transformed_pro) - res_int
 if (res_fra != 0 and res_int != 0):
  res = str(res_int) + "'" + str(res_fra)  # 返回分数
 else:
  res = str(eval(transformed_pro))  # 返回整数字符化

 return res #返回一个字符串形式的参数可能为整数，可能为真分数




def raise_ex(s1,s2):
 if(s1=='-n' and s2=='-r'):
  return True
 # print('主动抛出异常')
 ex = Exception('参数格式错误！')
 raise ex

def main():
 '''
 输入：
 - -n num：生成题目的数量num，若无此给出此参数，默认为10
 - -r num：生成题目的数的范围在[0, num)，必须给定。若未给定则报错
 输出：
 - - 作业习题文档
 - -e <exercisefile>.txt -a <answerfile>.txt：在当前目录中习题集和答案集的txt文档
 - -统计结果输出到文件Grade.txt
 '''
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
    float(n)
    float(r)
   except ValueError:
    print("num处输入的不是数字！")
   else:

    Exer=open('Exercises' + '.txt', "w")##创建两个txt文件
    Answ=open('Answers' + '.txt', "w")

    problem = gen_problem_list(n, r)
    answer=cal_problem_list(problem)

    for i in range(len(problem)):
     p = str(problem[i])
     p = str(i + 1) + '.  ' + p+' ='+ '\n'
     Exer.write(p)
    Exer.close()

    for j in range(len(answer)):
     s = str(answer[j])# 去除[],这两行按数据不同，可以选择
     s =str(j+1)+'.  '+s+ '\n'
     Answ.write(s)
    Answ.close()
    print(answer)


if __name__ == '__main__':
 main()

### 作用

#计算一个题目

### 接收参数

#- problem：题目，类型为list，格式为gen_problem的返回参数

### 返回参数