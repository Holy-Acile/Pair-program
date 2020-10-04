import re
from fractions import Fraction


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
