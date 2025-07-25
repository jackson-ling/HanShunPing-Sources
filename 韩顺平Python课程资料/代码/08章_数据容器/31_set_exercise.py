# @Version  : 1.0
# @Author   : 韩顺平

# 1、用三个集合表示三门学科的选课学生姓名(一个学生可以同时选多门课),
# s_history = {'小明', "张三", '李四', "王五", 'Lily', "Bob"}
# s_politic = {'小明', "小花", '小红', "二狗"}
# s_english = {'小明', 'Lily', "Bob", "Davil", "李四"}
#
# - 求选课学生总共有多少人
# - 求只选了第一个学科(history)的学生数量和学生名字
# - 求只选了一门学科的学生数量和学生名字
# - 求选了三门学科的学生数量和学生名字

# 定义3个集合
s_history = {'小明', "张三", '李四', "王五", 'Lily', "Bob"}
s_politic = {'小明', "小花", '小红', "二狗"}
s_english = {'小明', 'Lily', "Bob", "Davil", "李四"}

# - 求选课学生总共有多少人
"""
    思路分析
    1. 对三个集合求并集 【自动去重】
    2. 对新的集合求len()
"""
print(f"求选课学生总共有 {len(s_history | s_politic | s_english)}人")

# - 求只选了第一个学科(history)的学生数量和学生名字
"""
    思路分析
    1. 即求出只在s_history学员
    2. 使用差集即可   s_history - s_politic - s_english
"""
print(
    f"只选了第一个学科(history)的学生数量 {len(s_history - s_politic - s_english)}和学生名字 {s_history - s_politic - s_english}")

# - 求只选了一门学科的学生数量和学生名字
"""
    思路如下:
    1. 求出只选择了history的学生
    2. 求出只选择了politic的学生
    3. 求出只选择了english的学生
    4. 然后求并集集合
"""
# 1. 求出只选择了history的学生
s1 = s_history - s_politic - s_english
# 2. 求出只选择了politic的学生
s2 = s_politic - s_history - s_english
# 3. 求出只选择了english的学生
s3 = s_english - s_politic - s_history

print(f"只选了一门学科的学生数量 {len(s1 | s2 | s3)}和学生名字 {s1 | s2 | s3}")

# - 求选了三门学科的学生数量和学生名字
"""
    思路分析:
    1. 求出既在  s_politic 又在s_history 还在 s_english中
    2. 就是对三个集合求交集    
"""
print(f"选了三门学科的学生数量 {len(s_politic & s_history & s_english)}和学生名字 {s_politic & s_history & s_english}")
