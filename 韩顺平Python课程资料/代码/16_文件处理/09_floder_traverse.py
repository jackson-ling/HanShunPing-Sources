# @Version  : 1.0
# @Author   : 韩顺平


# 遍历某个文件夹，判断它们分别是目录还是文件

"""
    思路分析
    - 先考虑单级目录
    1. 获取文件夹(目录)的所有内容(元素), 包含了文件和目录
    2. 判断是文件还是目录, 输出对应的信息
"""

import os

# 指定要查看的目录
dir_path = "d:/a"
# # 获取文件夹(目录)的所有内容(元素)
# content_list = os.listdir(dir_path)
# # print("content_list:", content_list)
# # 遍历content_list, 输出对应的信息
# for ele in content_list:
#     child_ele = dir_path + "/" + ele
#     if os.path.isdir(child_ele):
#         print(f"目录: {child_ele}")
#     else:
#         print(f"文件: {child_ele}")

"""
    思路分析
    - 先考多级目录-递归的操作函数
    1. 获取文件夹(目录)的所有内容(元素), 包含了文件和目录
    2. 判断是文件还是目录, 输出对应的信息
    2.1 如果是目录, 则输出信息后，再递归处理
    2.2 如果是文件, 直接输出信息即可
"""


def print_dir_all_content(dir_path):
    # 获取文件夹(目录)的所有内容(元素)
    content_list = os.listdir(dir_path)
    # 遍历content_list, 输出对应的信息
    for ele in content_list:
        child_ele = dir_path + "/" + ele
        if os.path.isdir(child_ele):
            print(f"目录: {child_ele}")
            # 递归的操作
            print_dir_all_content(child_ele)
        else:
            print(f"文件: {child_ele}")


# 测试一下
print_dir_all_content(dir_path)
