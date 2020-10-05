import re
from module.cal_problem_list import cal_problem_list


def load(path):
    try:
        load_txt = [
            w.strip() for w in open(path, 'r', encoding='UTF-8').readlines()
        ]
    except IOError:
        print("Error: 没有从该路径：{}找到文件/读取文件失败".format(path))
    else:
        change = []
        for i in load_txt:
            input_pro = re.sub(r"(\d+\. )", r'', i)  # 去掉序号
            input_pro = input_pro.replace("=", '')  # 去掉等号
            # input_pro = re.sub(r"\s+", "", input_pro)#去掉空格
            change.append(input_pro)
        return change


def check(problem, answer):
    standard_ans = cal_problem_list(problem)
    #默认输入答案对仗
    wrong = []
    right = []
    for i in range(len(standard_ans)):
        if standard_ans[i] != answer[i]:
            wrong.append(str(i + 1))
        else:
            right.append(str(i + 1))
    correct_txt = 'Correct:' + str(len(right)) + '(' + ", ".join(
        str(i) for i in right) + ')'
    wrong_txt = 'Wrong:' + str(len(wrong)) + '(' + ", ".join(
        str(i) for i in wrong) + ')'
    Grade = open('Grade' + '.txt', "w", encoding='utf-8')
    Grade.write(correct_txt)
    Grade.write(wrong_txt)

    return print(correct_txt + '\n' + wrong_txt)
