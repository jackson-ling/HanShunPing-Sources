# @Version  : 1.0
# @Author   : 韩顺平

# 小头儿子 参加python考试, 他和 大头爸爸 达成承诺：
# 如果：
# 成绩为100分时，奖励一辆BMW；
# 成绩为(80，99]时，奖励一台iphone13；
# 当成绩为[60,80]时，奖励一个 iPad；
# 其它时，什么奖励也没有。
# 请从键盘输入小头儿子的期末成绩，并加以判断
"""
    思路分析
    1. 定义变量score 接收成绩 转成一个int
    2. 根据成绩进行判断，输出相应的提示信息即可
    3. 使用多分支搞定if - elif -.. else
"""
score = int(input("请输入成绩[整数]: "))
if 0 <= score <= 100:
    if score == 100:
        print("奖励一辆BMW")
    elif 80 < score <= 99:
        print("奖励一台iphone13")
    elif 60 <= score <= 80:
        print("奖励一个 iPad")
    else:
        print("啥也没有...")

else:
    print(score, "不在0~100")
