# @Version  : 1.0
# @Author   : 韩顺平

# 格式化输出案例
# 定义变量
age = 80
score = 77.5
gender = '男'
name = "贾宝玉"

# %操作符输出
print("个人信息: %s-%d-%s-%.2f" % (name, age, gender, score))

# format()函数
print("个人信息: {} {} {}".format(name, age, gender))

# f-strings[推荐]
print(f"个人信息: {name} {age} {score} {gender}")
