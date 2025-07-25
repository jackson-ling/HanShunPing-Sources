# @Version  : 1.0
# @Author   : 韩顺平


# for 遍历列表
"""
    思路分析
    1. 因为for循环是直接从列表中依次取出, 所以直接操作即可
    2. 每取出一个就输出/或者根据自己的业务处理
"""
list_color = ['red', 'green', 'blue', 'yellow', 'white', 'black']
for ele in list_color:
    print(f"元素是: {ele}")
