# @Version  : 1.0
# @Author   : 韩顺平


# f1是一个函数
def f1():
    for i in range(1, 5):
        if i == 3:
            # return就是跳出函数
            return
            # break
            # continue
        print("i =", i)
    print("结束了for..")


# 调用f1函数->执行f1函数
f1()
