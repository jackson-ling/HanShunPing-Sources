# @Version  : 1.0
# @Author   : 韩顺平


# 1、统计3个班成绩情况, 每个班有5名同学, 要求完成  [文件: stu_score.py]
# 1) 求出各个班的平均分和所有班级的平均分, 学生的成绩从键盘输入
# 2) 统计三个班及格人数
# 重要的编程思路: (1) 化繁为简 (2) 先死后活[先考虑3个班,每个班5名学生]
# 化繁为简
# 1.统计1个班成绩情况, 求出一个班的平均分
# 2.统计3个班成绩情况, 求出各个班的平均分、所有班级的平均分和及格人数

# 定义相关的变量
# 定义班级个数
class_num = 3
# 学生的个数
student_num = 5
# 统计一个班的总分
# sum = 0.0
# 统计所有班级的总分
total = 0.0
# 统计所有的及格人数
pass_num = 0

# 循环的处理3个班级的成绩:
for j in range(1, class_num + 1):

    # 统计1个班成绩情况, 求出一个班的平均分-for 循环5次，接收学员的成绩
    # 统计每个班的总分前，需要清0
    sum = 0.0
    for i in range(1, student_num + 1):
        score = float(input(f"请输入第 {j} 班的 第 {i}个 学生的成绩："))
        # 判断是否及格，累加到pass_num
        if score >= 60.0:
            pass_num += 1
        # 累加到sum
        sum += score
    print(f"第 {j} 班级的情况: 平均分 {sum / 5}")
    # 将sum累加到 total
    total += sum

# 输出所有班级的平均分和及格人数
print(f"所有班级的平均分 {total / (student_num * class_num)} 及格人数: {pass_num}")
