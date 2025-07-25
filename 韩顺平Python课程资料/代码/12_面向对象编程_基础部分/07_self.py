# @Version  : 1.0
# @Author   : 韩顺平

class Dog:
    name = "波斯猫"
    age = 2

    def info(self, name):
        print(f"name信息: {name}")  # ?加菲猫
        # 通过self.属性名 可以访问 对象的属性/成员变量
        print(f"属性name: {self.name}") # 波斯猫


dog = Dog()
dog.info("加菲猫")


# class Dog:
#     name = "藏獒"
#     age = 2
#
#     def info(self, name):
#         print(f"name信息->{name}")
#
#     # 静态方法
#     # 老师解读:
#     # 1.通过@staticmethod 可以将方法转为静态方法
#     # 2.如果是一个静态方法, 可以不带self
#     # 3. 静态的方法的调用形式有变化
#     @staticmethod
#     def ok():
#         print("ok()...")
#
#
# dog = Dog()
# dog.info("德牧")
# # 调用静态方法
# # 方式1: 通过对象调用
# dog.ok()
# # 方式2: 通过类名调用
# Dog.ok()


# self表示当前对象本身, 简单的说，哪个对象调用，self就代表哪个对象
# class Dog:
#     name = "藏獒"
#     age = 2
#
#     def hi(self):
#         print(f"hi self: {id(self)}") # 自身
#
#
# # self表示当前对象本身
# # 创建对象dog2
# dog2 = Dog()
# print(f"dog2: {id(dog2)}")
# dog2.hi()
# # 创建对象dog3
# print("--------------------")
# dog3 = Dog()
# print(f"dog3: {id(dog3)}")
# dog3.hi()


# 在方法内部, 要访问成员变量和成员方法, 需要使用self
class Dog:
    name = "藏獒"
    age = 2

    def eat(self):
        print(f"{self.name} 饿了..") # 中华田园犬 饿了..

    def cry(self, name):
        print(f"{name} is crying") # 金毛 is crying
        print(f"{self.name} is crying") # 中华田园犬 is crying
        self.eat() #self
        # 不能直接调用
        # eat()


dog = Dog()
# 修改 dog对象的属性name=> 中华田园犬
dog.name = "中华田园犬"
dog.cry("金毛")


