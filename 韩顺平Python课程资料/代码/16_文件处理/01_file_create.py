# @Version  : 1.0
# @Author   : 韩顺平


# 演示创建文件, 在d的a目录下创建 hi.txt 文件
"""
    老师说明: 如果我们要创建一个文件, 只需要以 mode="w" 形式打开文件即可
    如果, 该文件不存在, 系统就会创建该文件
    注意: encoding="utf-8" 是关键字参数, 不能少 encoding, 因为 encoding 并不是open() 方法的第3个形参
"""
f1 = open("d://a//hi.txt", "w", encoding="utf-8")
print(f"文件创建成功类型是: {type(f1)}")
