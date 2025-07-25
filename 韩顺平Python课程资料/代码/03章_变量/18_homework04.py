# @Version  : 1.0
# @Author   : 韩顺平


# 4、编程实现如下效果 homework04.py
#      姓名   年龄        成绩   性别   爱好
#      xx     xx        xx     xx     xx
# 要求：
# 1) 用变量将姓名、年龄、成绩、性别、爱好存储
# 2) 使用+
# 3) 添加适当的注释
# 4) 添加转义字符, 使用一条语句输出

# 定义需要的变量
name = "jack"
age = 20
score = 90.2
gender = "男"
hobby = "打篮球"

# 按照规定的格式输出信息
print("姓名\t\t年龄\t\t成绩\t\t性别\t\t爱好\n" + name
      + "\t" + str(age) + "\t\t" + str(score)
      + "\t" + gender + "\t\t" + hobby)
