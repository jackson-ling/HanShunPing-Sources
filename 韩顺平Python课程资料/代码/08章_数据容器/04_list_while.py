# @Version  : 1.0
# @Author   : 韩顺平

# while 遍历列表
"""
    思路分析
    1. 先定义变量index = 0 表示从第一个元素开始取出
    2. 列表list_color的个数 6 , 这里其实有一个内置函数 len(列表), 可以返回个数
    3. 每取出一个就输出/或者根据自己的业务处理
"""
list_color = ['red', 'green', 'blue', 'yellow', 'white', 'black']

# 得到list的元素个数
# print(len(list_color))  # 6
# 先定义变量index = 0 表示从第一个元素开始取出
index = 0
while index < len(list_color):
    print(f"第 {index + 1} 个元素的是: {list_color[index]}")
    index += 1


