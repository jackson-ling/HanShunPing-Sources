# @Version  : 1.0
# @Author   : 韩顺平

# 编写类Book,  定义方法update_price，
# 实现更改某本书的价格，
# 具体：如果价格>150,则更改为150，如果价格>100,更改为100，否则不变

"""
    类名: Book
    属性: name,price
    构造器: __init__(self,name,price)
    方法: update_price 完成功能： 如果价格>150,则更改为150，如果价格>100,更改为100，否则不变
"""


class Book:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def update_price(self):
        # 如果价格 > 150, 则更改为150，如果价格 > 100, 更改为100，否则不变
        if self.price > 150:
            self.price = 150
        elif self.price > 100:
            self.price = 100

    # 增加一个输出书籍信息的方法
    def info(self):
        print(f"书的信息 {self.name} {self.price}")


# 测试
book = Book("天龙八部", 50)
book.info()
book.update_price()
book.info()
