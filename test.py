import re
from fractions import Fraction
'''
1.乘号除号替换
2.真分数包含‘的要替换为加号
3.分数要用小括号括起来
'''
input_text = " 1'1/3 × 5 "
t1="'"#先处理假分数
if(t1 in input_text):
 input_text = re.sub(r"(\d+'\d+/\d+)", r'(\1)', input_text)
 input_text=input_text.replace("'",'+')

input_text = re.sub(r'(\d+/\d+)', r'(\1)', input_text)#将再将分数优先处理
print(input_text)

t2="÷"
if(t2 in input_text):
 input_text=input_text.replace("÷",'/')

t3="×"
if(t3 in input_text):
 input_text=input_text.replace("×",'*')


transformed_text = re.sub(r'(\d+)', r'Fraction("\1")', input_text)#小数转分数
print(transformed_text)

results = eval(transformed_text)
print(results)

