#all ok!!！

import re
from fractions import Fraction
import sys

from module.cal_problem_list import cal_problem_list
from module.gen_problem_list import gen_problem_list


# 主动抛出异常
def raise_ex(s1, s2):
    if (s1 == '-n' and s2 == '-r'):
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
            print(raise_ex(s1, s2))
        except Exception as re:
            print(re)
        else:
            try:
                int(n)
                int(r)
            except ValueError:
                print("Error:num处输入的不是整数！")
            else:
                Exer = open('Exercises' + '.txt', "w",
                            encoding='utf-8')  ##创建两个txt文件
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


if __name__ == '__main__':
    main()
