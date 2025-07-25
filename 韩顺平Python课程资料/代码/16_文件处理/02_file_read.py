# @Version  : 1.0
# @Author   : 韩顺平

# 参考
# 需求: 读取在d盘的a目录下 hello.txt 文件, hello.txt已经存在


# 打开文件
f = open("d://a//hello.txt", "r", encoding="utf-8")

# 读取方式1: read(), 一次返回整个文件的内容
# content = f.read()
# 请思考如果执行 f.read(6) 会读取到什么内容, 分析一下
# content = f.read(6) #content: # 列表的定
# 关闭文件, 释放文件占用的系统资源
# f.close()
#
# print("==========hello.txt内容============")
# print(content)


# # 读取方式2: f.readline(), 注意readline, 字符串末尾保留换行符\n
# print("==========hello.txt内容 方式2============")
#
# f.readline()的使用
# line1 = f.readline()  # # 列表的定义\n
# line2 = f.readline()  # """\n
# print(f"第1行数据是{line1}")
# print(f"第2行数据是{line2}")
# f.close()
#
# # 循环读取整个文件, 一行行的读取
# while True:
#     line_content = f.readline()
#     if line_content == "":  # 如果为"" ,表示文件读取完毕
#         break
#     print(line_content, end="")
#
# f.close()

# # 读取方式3: f.readlines()列表形式读取文件中的所有行
# lines = f.readlines()
# print(f"lines类型是->{type(lines)}") #list
# print(f"lines内容是->{lines}") #["第一行的数据\n", "第2行的数据\n"...]
# for line in lines:
#     print(line, end="")
# f.close()

# 读取方式4: for line in f形式读取文件
for line in f:
    print(line, end="")
f.close()
