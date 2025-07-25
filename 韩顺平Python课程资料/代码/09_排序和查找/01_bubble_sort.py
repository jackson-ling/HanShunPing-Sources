# @Version  : 1.0
# @Author   : 韩顺平

"""
    下面我们举一个具体的案例来说明冒泡法, 列表：[24,69,80,57,13] 有5个元素,
    使用冒泡排序法将其排成一个从小到大的有序列表
"""

# 老韩说明, 如果只是完成排序功能, 我们可以直接使用list的方法sort, 如下

# 排序的列表
num_list = [24, 69, 80, 57, 13, 0, 900, -1, -300, 9]
print("排序前".center(32, "-"))
print(f"num_list: {num_list}")


# 使用sort方法完成排序
# num_list.sort()
# print("排序后".center(32, "-"))
# print(f"num_list: {num_list}")


# 使用冒泡排序, 自己完成排序, 目的了解底层原理, 深刻理解
# (以后遇到不同业务, 需要定制排序, 也能处理)

# 定义函数-完成排序
def bubble_sort(my_list):
    """
    功能: 对传入的列表排序-顺序是从小到大
    :param my_list: 传入的列表
    :return: 无
    """
    """
        通过分析,我们发现每一轮的比较逻辑是一样的
        ,我们只需要考虑变化的部分即可，使用外层的for循环来处理
    """
    # i变量来控制多少轮排序 len(my_list) - 1
    for i in range(0, len(my_list) - 1):
        # j变量控制比较的次数, 同时可以作为比较元素的索引下标
        for j in range(0, len(my_list) - 1 - i):
            # 如果前面的元素 > 后面的元素, 就交换
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

        # print(f"第{i + 1}轮排序后的结果 my_list: ", my_list)

    """
        第一轮排序: 把最大的数放到最后的位置
        第1次比较: [24, 69, 80, 57, 13]
        第2次比较: [24, 69, 80, 57, 13]
        第3次比较: [24, 69, 57, 80, 13]
        第4次比较: [24, 69, 57, 13, 80]
    """
    # j变量控制比较的次数, 同时可以作为比较元素的索引下标
    # for j in range(0, 4):  # [0,1,2,3]
    #     # 如果前面的元素 > 后面的元素, 就交换
    #     if my_list[j] > my_list[j + 1]:
    #         my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    #
    # print("第1轮排序后的结果 my_list", my_list)

    """
        第二轮排序: 把第二大数放到倒数第二的位置
        第1次比较: [24, 69, 57, 13, 80]
        第2次比较: [24, 57, 69, 13, 80]
        第3次比较: [24, 57, 13, 69, 80]

    """
    # j变量控制比较的次数, 同时可以作为比较元素的索引下标
    # for j in range(0, 3):  # [0,1,2]
    #     # 如果前面的元素 > 后面的元素, 就交换
    #     if my_list[j] > my_list[j + 1]:
    #         my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    #
    # print("第2轮排序后的结果 my_list", my_list)

    """
        第三轮排序: 把第三大数放到倒数第三的位置
        第1次比较: [24, 57, 13, 69, 80]
        第2次比较: [24, 13, 57, 69, 80]
    """

    # j变量控制比较的次数, 同时可以作为比较元素的索引下标
    # for j in range(0, 2):  # [0,1]
    #     # 如果前面的元素 > 后面的元素, 就交换
    #     if my_list[j] > my_list[j + 1]:
    #         my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    #
    # print("第3轮排序后的结果 my_list", my_list)

    """
        第四轮排序: 把第四大数放到倒数第四的位置
        第1次比较: [13, 24, 57, 69, 80]
    """

    # j变量控制比较的次数, 同时可以作为比较元素的索引下标
    # for j in range(0, 1):  # [0]
    #     # 如果前面的元素 > 后面的元素, 就交换
    #     if my_list[j] > my_list[j + 1]:
    #         my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    #
    # print("第4轮排序后的结果 my_list", my_list)


bubble_sort(num_list)
print("排序后".center(32, "-"))
print(f"num_list: {num_list}")


