# @Version  : 1.0
# @Author   : 韩顺平

# 使用while和for遍历字符串
str_b = "hi-韩顺平教育"
# while循环遍历
# 表示从第一个元素开始遍历
index = 0
while index < len(str_b):
    print(f"第 {(index + 1)} 个元素是: {str_b[index]}")
    # 循环控制遍历增1
    index += 1

# print("==================")
# 上面的分隔符可以这样写
print("=" * 30)
#
# for循环遍历
for ele in str_b:
    print(ele)
