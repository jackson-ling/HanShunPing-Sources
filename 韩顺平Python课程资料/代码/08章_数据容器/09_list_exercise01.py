# @Version  : 1.0
# @Author   : 韩顺平


# 循环从键盘输入5个成绩，保存到列表,并输出
"""
    思路分析：
    1. 定义一个空列表保存成绩 scores = []
    2. 循环操作5次, 接收用户的输入, 每接收一个数据就添加到scores
    3. 输出成绩即可
"""
# 定义一个空列表保存成绩 scores = []
scores = []
# 循环输入成绩
for _ in range(5):
    score = float(input("请输入成绩: "))
    scores.append(score)

# 输出成绩情况
print("成绩情况是：", scores)
