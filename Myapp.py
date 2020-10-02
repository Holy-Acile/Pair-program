import re
from fractions import Fraction


def cal_problem(input_pro):
 '''
 1.乘号除号替换
 2.真分数包含‘的要替换为加号
 3.分数要用小括号括起来
 '''
 input_pro = re.sub(r'(\d+/\d+)', r'(\1)', input_pro)  # 将整体字符串中的真分数括起来

 t1 = "'"
 if (t1 in input_pro):
  input_pro = input_pro.replace("'", '+')

 t2 = "÷"
 if (t2 in input_pro):
  input_pro = input_pro.replace("÷", '/')

 t3 = "×"
 if (t3 in input_pro):
  input_pro = input_pro.replace("×", '*')


 transformed_pro = re.sub(r'(\d+)', r'Fraction("\1")', input_pro)  # 小数转分数
 print(transformed_pro)

 res_int = int(eval(input_pro))
 res_fra = eval(transformed_pro)-res_int
 if (res_fra!=0):
  res=str(res_int)+"'"+str(res_fra)#返回分数
 else:
  res=eval(transformed_pro)#返回整数

 return res#返回一个参数可能为整数，可能为真分数