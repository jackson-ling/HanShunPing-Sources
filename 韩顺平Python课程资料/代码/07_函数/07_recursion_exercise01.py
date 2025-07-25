# @Version  : 1.0
# @Author   : 韩顺平

# 请使用递归的方式求出斐波那契数1,1,2,3,5,8,13...给你一个整数n，求出它的值是多

def fbn(n):
    """
    功能: 返回n对应的斐波那契数
    :param n: 接收一个整数n>=1
    :return: 返回斐波那契数
    """
    if n == 1 or n == 2:
        return 1
    # 如果n >2 则对应的斐波那契数为 n-1 和 n-2对应的斐波那契数的和
    else:
        return fbn(n - 1) + fbn(n - 2)


# 完成测试
print(fbn(7))  # 13
