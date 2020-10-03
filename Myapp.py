#answer okk

import re
from fractions import Fraction

def cal_problem_list(problem_list):
 '''
 输入：题目集problem_list
 输出：答案集answer_list
 '''
 answer_list=[]
 for problem in problem_list:
  cal_re=cal_problem(problem)
  answer_list.append(cal_re)

 return answer_list

def cal_problem(input_pro):
 '''
 输入：表达式字符串
 输出：计算后字符串
 1.乘号除号替换
 2.真分数包含‘的要替换为加号
 3.分数要用小括号括起来
 4.大于1的真分数的需要整体括起来
 '''
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
 print(transformed_pro)

 res_int = int(eval(input_pro))
 res_fra = eval(transformed_pro) - res_int
 if (res_fra != 0 and res_int != 0):
  res = str(res_int) + "'" + str(res_fra)  # 返回分数
 else:
  res = str(eval(transformed_pro))  # 返回整数字符化

 return res  # 返回一个字符串形式的参数可能为整数，可能为真分数

def main():
 problem = ["5+1", "1/2 ÷ 3", "1'1/3 × 5"]
 re=cal_problem_list(problem)
 print(re)


if __name__ == '__main__':
 main()