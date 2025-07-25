# @Version  : 1.0
# @Author   : 韩顺平

# 1、切片语法: 序列[起始索引:结束索引:步长], 起始索引如果不写, 默认为0, 结束索引如果不写,
# 默认为截取到结尾, 步长如果不写, 默认为1

str = "hello,韩顺平教育"
str_slice01 = str[:5:1]
print("str_slice01->", str_slice01)  # hello

str_slice02 = str[1::1]
print("str_slice02->", str_slice02)  # ello,韩顺平教育

str_slice03 = str[::1]
print("str_slice03->", str_slice03)  # hello,韩顺平教育

str_slice04 = str[2:5:]
print("str_slice04->", str_slice04)  # llo

# 切片语法: 序列[起始索引:结束索引:步长], 步长为负数,
# 表示反向取, 同时注意起始索引和结束索引也要反向标记

str = "123456"
str_slice05 = str[-1::-1]
print("str_slice05->", str_slice05)  # 654321

str_slice06 = str[-1:-6:-1]
print("str_slice06->", str_slice06)  # 65432

# 切片操作并不会影响原序列，而是返回了一个序列,
str = "ABCD"
str_slice07 = str[1:3:1]  # BC
print(f"str->{str} str_slice07->{str_slice07}")  # "ABCD" "BC"
