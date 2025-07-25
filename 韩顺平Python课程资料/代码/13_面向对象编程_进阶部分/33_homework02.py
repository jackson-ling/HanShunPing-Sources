# @Version  : 1.0
# @Author   : 韩顺平

"""
    文件中有 Grand 、Father 和 Son ，
    问：父类和子类中通过self和super()都可以调用哪些属性和方法
"""


class Grand:
    """
    Grand类
    """
    name = "AA"
    __age = 100

    def g1(self):
        print("Grand-g1()")


class Father(Grand):
    id = "001"
    __score = None

    def f1(self):
        """
        :return:
        """
        # super() 可以访问哪些成员(属性和方法）?
        # 填写? super().name super().g1()
        # self可以访问哪些成员?
        # 填写? self.id self.__score self.f1() self.name self.g1()
        print("Father-f1()...")


# Son类
class Son(Father):
    name = "BB"

    def g1(self):
        print("Son-g1()")

    def __show(self):
        # super() 可以访问哪些成员(属性和方法)?
        # 填写: super().id super().f1() super().name super().g1()
        # self可以访问哪些成员?
        # 填写 self.name self.g1() self.__show() self.id self.f1()
        print("Son-__show()...")


# 测试
"""
    思路分析
    1. 继承关系是 Son->Father->Grand
"""
