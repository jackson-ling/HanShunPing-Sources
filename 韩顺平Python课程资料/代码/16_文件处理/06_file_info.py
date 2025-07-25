# @Version  : 1.0
# @Author   : 韩顺平





# 参考
# 获取文件相关信息(大小、创建时间、访问时间、修改时间等)
"""
    说明:
    time.ctime()方法的作用则是将返回来的时间戳转为字符串格式
"""
import os
import time

f_stat = os.stat("d:/a/hello.txt")
print("--------文件信息---------")
print(f"文件大小->{f_stat.st_size} \n"
      f"最近的访问时间->{time.ctime(f_stat.st_atime)} \n"
      f"最近的修改时间->{time.ctime(f_stat.st_mtime)} \n"
      f"文件创建时间->{time.ctime(f_stat.st_ctime)}")


