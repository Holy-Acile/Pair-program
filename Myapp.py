#all ok!!！
import os
import re
from fractions import Fraction
import sys

from module.cal_problem_list import cal_problem_list
from module.gen_problem_list import gen_problem_list
from module.check_txt import load, check


# 主动抛出异常
def raise_ex(s1, s2):
    if (s1 == '-n' and s2 == '-r'):
        return 1
    elif (s1 == '-e' and s2 == '-a'):
        return 2
    else:
        ex = Exception('Error:参数格式错误！')
        raise ex


def making_problem(n, r):
    try:
        int(n)
        int(r)
    except ValueError:
        print("Error:num处输入的不是整数！")
    else:
        Exer = open('Exercises' + '.txt', "w", encoding='utf-8')  ##创建两个txt文件
        Answ = open('Answers' + '.txt', "w", encoding='utf-8')
        n = int(n)
        r = int(r)
        problem = gen_problem_list(n, r)
        print(problem)
        answer = cal_problem_list(problem)

        for i in range(len(problem)):
            p = str(problem[i])
            p = str(i + 1) + '. ' + p + ' = ' + '\n'
            Exer.write(p)
        Exer.close()

        for j in range(len(answer)):
            s = str(answer[j])
            s = str(j + 1) + '. ' + s + '\n'
            Answ.write(s)
        Answ.close()
        print(answer)


def main():
    try:
        s1, n, s2, r = sys.argv[1:5]
    except BaseException:
        print("Error: 输入命令错误")  # \n正确格式为-n num -r num \n
    else:
        try:
            res = raise_ex(s1, s2)
        except Exception as re:
            print(re)
        else:
            if (res == 1):
                making_problem(n, r)
            elif (res == 2):
                e = n
                a = r
                load_e = load(e)
                load_a = load(a)
                check(load_e, load_a)
            # else:
            #     print('Error:选择错误')


if __name__ == '__main__':
    main()
