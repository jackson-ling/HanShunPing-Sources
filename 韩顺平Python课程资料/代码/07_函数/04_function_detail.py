# @Version  : 1.0
# @Author   : 韩顺平

# # 函数中的变量是局部的，函数外不生效
# def hi():
#     n = 10
#     print("n:", n)
#
#
# hi()
# # 函数内部定义的n, 在函数外部不能使用
# print("n:", n)


# 如果同一个文件, 出现两个函数名相同的函数, 则以就近原则进行调用.

# def cry(n):
#     print("cry()..hi...", n)
#
#
# def cry():
#     print("cry()..ok...")
#
#
# # 这个cry会默认就近原则,即第二个cry()
# cry()

# 5、调用函数时, 根据函数定义的参数位置来传递参数, 这种传参方式就是位置参数,
# 传递的实参和定义的的形参顺序和个数必须一致,
# 同时定义的形参, 不需要指定数据类型, 会根据传入的实参决定

# def car_info(name, price, color):
#     print(f"name->{name} price->{price} color->{color}")


# 传递的实参和定义的的形参顺序和个数必须一致, 否则报 TypeError 错误
# car_info("宝马", 500000, "red", 11)

# 6、函数可以有多个返回值
# 比如函数接收两个数, 返回这两个数的和、差
# def f2(n1, n2):
#     return n1 + n2, n1 - n2
#
#
# r1, r2 = f2(10, 20)
# print(f"r1->{r1} r2->{r2}")

# 7、函数支持关键字参数, 即: 函数调用时, 可以通过 "形参名=实参值" 形式传递参数,
# 这样可以不受参数传递顺序的限制

# def book_info(name, price, author, amount):
#     print(f"name->{name} price->{price} author->{author} amount->{amount}")


# 通常调用方式, 一一对应
# book_info("红楼梦", 60, "曹雪芹", 30000)
# book_info("红楼梦", 60, 30000, "曹雪芹")

# 关键字参数
# print("------------关键字参数------------")
# book_info(name="红楼梦", price=60, amount=30000, author="曹雪芹")
# book_info("红楼梦", 60, amount=6000, author="曹雪芹")


# 8、函数支持默认参数/缺省参数
# - 定义函数时, 可以给参数提供默认值, 调用函数时, 指定了实参, 则以指定为准, 没有指定, 则以默认值为准
def book_info2(name='<<thinking in python>>', price=66.8, author='龟叔', amount=1000):
    print(f"name->{name} price->{price} author->{author} amount->{amount}")


# 调用测试
# book_info2()
# book_info2('<<study python>>')


# - 默认参数, 需要放在参数列表后
# def book_info3(name, price, author='龟叔', amount=1000):
#     print(f"name->{name} price->{price} author->{author} amount->{amount}")

# 调用测试
# book_info3("<<python 揭秘>>", 999)


# 错误的写法
# def book_info4(author='龟叔', amount=1000, name, price):
#     print(f"name->{name} price->{price} author->{author} amount->{amount}")


# 函数支持可变参数/不定长参数,  应用场景: 当调用函数时, 不确定传入多少个实参的情况
# 比如我们要计算多个数的和, 但是不确定是几个数 *[0到多]
# def sum(*args):
#     # 输出了args的数据和类型 (1, 2)
#     print(f"args->{args} 类型是->{type(args)}")
#     total = 0
#     # 对args进行遍历, 即对元组tuple遍历
#     for ele in args:
#         total += ele
#     return total


# 调用测试
# result = sum(1, 2)
# print(f"result->{result}")

# result = sum(1, 2, 3, -10)
# print(f"result->{result}")

# result = sum()
# print(f"result->{result}")


# 10、函数的可变参数/不定义参数 还支持多个关键字参数, 也就是 多个 "形参名=实参值"
# - 应用场景: 当调用函数时, 不确定传入多少个 关键字参数 的情况
# - 传入的多个关键字参数, 会被组成一个字典(dict), 后面会详细讲解字典, 这里简单的了解下
# - 简单说明: 字典可以储存多个 键=值  的数据项

# 比如我们需要接收一个人的信息,但是有哪些信息是不确定的, 就可以使用关键字可变参数(**args)
def person_info(**args):
    # 输出args的数据 {'name': 'hsp', 'age': 18, 'email': 'hsp@qq.com'}和 类型
    print(f"args->{args} 类型->{type(args)}")
    # 遍历args, 是一个字典, 下面的arg_name就是取出各个参数名,
    # args[arg_name]就是取出参数值
    for arg_name in args:
        print(f"参数名->{arg_name} 参数值->{args[arg_name]}")


# 测试
person_info(name="hsp", age=18, email="hsp@qq.com")
# person_info(name="hsp", age=18, email="hsp@qq.com", sex="男", address="北京")
# person_info()
