# @Version  : 1.0
# @Author   : 韩顺平

# 演示字符串常用操作
str_names = "jack tom mary hsp nono tom"
# len(str): 字符串的长度, 也就是包含多少个字符
print(f"{str_names} 有 {len(str_names)} 个字符")

# str.replace(old, new[, count]): 返回字符串的副本，其中出现的所有子字符串 old 都将被替换为 new。
# 如果给出了可选参数 count，则只替换前 count 次出现
"""
    老韩说明:返回字符串的副本 表示原来的字符串不变, 而是返回一个新的字符串, 
    可以画一个示意图
"""
# 需求: 将"jack" 替换成 "杰克", 只替换一个
str_names_new = str_names.replace("jack", "杰克", 1)
print("str_names_new:", str_names_new)  # "杰克 tom mary hsp nono tom"
print("str_names:", str_names)  # "jack tom mary hsp nono tom"

# str.split(sep=None, maxsplit=- 1):
# 返回一个由字符串内单词组成的列表，使用 sep 作为分隔字符串。 如果给出了 maxsplit，
# 则最多进行 maxsplit 次拆分（因此，列表最多会有 maxsplit+1 个元素）。 如果 maxsplit
# 未指定或为 -1，则不限制拆分次数（进行所有可能的拆分）

# 需求对str_names按照" "进行分割
str_names_split = str_names.split(" ")
print(f"str_names_split 内容是 {str_names_split} 类型是: {type(str_names_split)}")  # [jack tom mary hsp nono tom] list
print(f"str_names 内容是: {str_names}")  # "jack tom mary hsp nono tom"

# str.count(sub): 统计指定字符串在字符串中出现的次数
# 统计tom在字符串出现了几次
print("tom在字符串出现的次数:", str_names.count("tom"))  # 2

# str.index(sub): 从字符串中找出指定字符串第一个匹配项的索引位置
print(f"tom出现的索引是: {str_names.index('tom')}")  # 5

# str.strip([chars]):  返回原字符串的副本，移除其中的前导和末尾字符。 chars 为指定要移除字符的字符串
# 老韩说明: 这个方法，通常可以用于除去前后的空格, 或者去掉指定的某些字符
# 需求, 去掉字符的前后的空格
str_names_strip = str_names.strip(" ")
print("str_names_strip:", str_names_strip)

# print("123t123om321".strip("132")) #tom

# str.lower(): 返回原字符串小写的副本, 不影响原来的字符
# 需求: 将字符串字母全部改成小写
str_names = "hspHSP"
str_names_lower = str_names.lower()
print("str_names_lower:", str_names_lower)  # hsphsp
print("str_names:", str_names)  # "hspHSP"

# str.upper(): 返回原字符串大写的副本, 不影响原来的字符
# 需求: 将字符串字母全部改成大写
str_names_upper = str_names.upper()
print("str_names_upper:", str_names_upper)  # HSPHSP
print("str_names:", str_names)  # hspHSP
