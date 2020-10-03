import os
def new_txt():

    open('answer1'+'.txt', "w")

if __name__ == '__main__':
    new_txt()

    '''
for j in range(len(answer)):
  s = str(answer[j]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
  s = s.replace('"', '').replace(',', '')  # 去除单引号，逗号，每行末尾追加换行符
  s =str(j+1)+'.  '+s+ '\n'
  Answ.write(s)
 Answ.close()
 
 # print('题目已展示在Exercises.txt文件中')
 # print('请作答！！')
 # print('----------------------------')
 # print('作答时，请按照**格式进行输入：')
    '''
    str=123
    try:
     f = float(str)
    except ValueError:
     print("输入的不是数字！")

    def input_password():
        # 提示用户输入密码
        pwd = input("请输入密码：")
        # 如果密码长度>=8,返回用户输入的密码
        if len(pwd) >= 8:
            return pwd
        # 如果 < 8 主动抛出异常
        print("主动抛出异常")
        # 1> 创建异常对象
        ex = Exception("密码长度不够")
        # 2> raise 主动抛出异常
        raise ex


    # 提示用户输入密码
    try:
        print(input_password())
    except Exception as result:
        print(result)