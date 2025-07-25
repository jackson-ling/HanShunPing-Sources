# @Version  : 1.0
# @Author   : 韩顺平


# f.flush() : 刷新流的写入缓冲区
import time

f = open("d://a//hi.txt", "w", encoding="utf-8")
f.write("你好1, python~\n")
f.write("你好2, python~\n")
f.write("你好3, python~\n")

# 测试f.flush()将缓冲区数据刷新, 写入文件
f.flush()
print("----等待----")
time.sleep(100000)
print("----等待 end----")


# 3、with open() as f:
# 在处理文件对象时，子句体结束后，文件会自动关闭

with open("d:/a/hello.txt", "r", encoding="UTF-8") as f:
    lines = f.readlines()
    print("----文件内容-----")
    for line in lines:
        print(line, end="")

print("\n文件是否关闭->", f.closed)
