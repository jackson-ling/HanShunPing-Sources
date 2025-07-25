# @Version  : 1.0
# @Author   : 韩顺平


# 通过父类名访问父类成员

class A:
    n1 = 100

    def run(self):
        print("A-run()....")


class B(A):
    n1 = 200

    def run(self):
        print(f"B-run()....")

    # say方法 通过父类名 去访问父类的成员
    def say(self):
        print(f"父类的n1 {A.n1}  本类的n1 {self.n1}")  # 100 200
        # 调用父类的run
        A.run(self)  # A-run()....
        # 调用本类的run
        self.run()  # B-run()....

    # hi方法, 通过super() 方式去访问父类成员
    def hi(self):
        print(f"父类的n1 {super().n1}")  # 100
        # 调用父类的run
        super().run()  # A-run()....


b = B()
# b.say()
# print("--------------")
b.hi()
