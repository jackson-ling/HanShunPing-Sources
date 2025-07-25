# @Version  : 1.0
# @Author   : 韩顺平

# while 遍历元组
tuple_color = ('red', 'green', 'blue', 'yellow', 'white', 'black')

# index=0表示从第一个元素进行遍历
index = 0
while index < len(tuple_color):
    print(f"第{index + 1}个元素的值: {tuple_color[index]}")
    index += 1
