# @Version  : 1.0
# @Author   : 韩顺平

# 说明：将一张图片/一首歌 拷贝到另外一个目录下,
# 要求使用read()和write()原生方法完成

"""
    思路分析
    1. 打开源文件(要拷贝的文件), 读取源文件的数据
    2. 打开目标文件(需要把文件拷贝到哪去), 把读取的文件数据写入目标文件即可
    3. 注意: 因为图片/音频是二进制文件，需要以二进制的方式打开
"""

# 源文件
f_src_path = "C:/Users/Administrator/Pictures/Saved Pictures/13.jpg"
# f_src_path = "C:/Users/Administrator/Music/无名.mp3"
# 目标文件
f_dst_path = "d:/a/13_new.jpg"
# f_dst_path = "d:/a/无名_new.mp3"

# # 打开源文件
# f_src = open(f_src_path, "rb")
# # 读取源文件的数据
# data = f_src.read()
#
# # 打开目标文件
# f_dst = open(f_dst_path, "wb")
# # 把读取的文件数据写入目标文件即可
# f_dst.write(data)
#
# # 关闭文件
# f_dst.close()
# f_src.close()
# print("拷贝OK...")

# 我们再使用with子句的方式完成文件拷贝(读取一行数据, 就写入)， 代码比较简洁

with open(f_src_path, "rb") as f_src:
    with open(f_dst_path, "wb") as f_dst:
        for data in f_src:
            f_dst.write(data)

print("拷贝OK....")