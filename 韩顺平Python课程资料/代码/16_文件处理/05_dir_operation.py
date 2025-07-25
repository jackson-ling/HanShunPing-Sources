# @Version  : 1.0
# @Author   : 韩顺平

"""
    演示目录操作
    1) 创建一级目录 d://aaa
    2) 创建多级目录 d://bbb//ccc
    3) 删除目录 d://aaa 和 d://bbb//ccc
"""

# 根据老师给出的相关函数, 即可搞定

# 1) 创建一级目录 d://aaa
import os

#
# if os.path.isdir("d://aaa"):
#     print("d://aaa 目录已经存在...")
# else:
#     os.mkdir("d://aaa")


# 2) 创建多级目录 d://bbb//ccc
# if os.path.isdir("d://bbb//ccc"):
#     print("d://bbb//ccc 目录已经存在...")
# else:
#     os.makedirs("d://bbb//ccc")

# 3) 删除目录 d://aaa 和 d://bbb//ccc
# 删除单级目录使用rmdir, 要求目录为空
# if os.path.isdir("d://aaa"):
#     os.rmdir("d://aaa")
# else:
#     print("d://aaa 目录不存在, 无法删除")

# 删除多级目录使用removedirs, 要求目录为空
if os.path.isdir("d://bbb//ccc"):
    os.removedirs("d://bbb//ccc")
else:
    print("d://bbb//ccc 目录不存在, 无法删除")
