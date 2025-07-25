# @Version  : 1.0
# @Author   : 韩顺平

# 1、定义一个字符串, str_names = "tom jack mary nono smith hsp" , str_exercise.py
# - 统计一共有多少个人名
# - 如果有 "hsp" 则替换成 "老韩"
# - 如果人名是英文，则把首字母改成大写

"""
    统计一共有多少个人名
    思路分析
    1. 使用split方法进行分割 " "
    2. 然后统计有多个人名即可

"""
str_names = "tom jack mary nono smith hsp"
str_names_list = str_names.split(" ")
print(f"一共有 {len(str_names_list)} 人名")  # 6

# 如果有 "hsp" 则替换成 "老韩"
str_names_re = str_names.replace("hsp", "老韩")
print(f"替换后的结果是 {str_names_re}")

# 如果人名是英文，则把首字母改成大写
"""
    思路分析
    "tom jack mary nono smith hsp 张三" => "Tom Jack Mary Nono Smith Hsp 张三"
    1. 定义字符串 str_names_upper 来保存新的结果
    2. 遍历 str_names_list 列表如果发现是英文名, 则将其首字母改成大写str.capitalize
    3. 拼接到 str_names_upper即可
"""
str_names_upper = ""
for element in str_names_list:
    if element.isalpha():
        str_names_upper += element.capitalize() + " "

# 去掉两边的" "
str_names_upper = str_names_upper.strip(" ")
print(f"如果人名是英文，则把首字母改成大写 处理结果是: {str_names_upper}")
