# @Version  : 1.0
# @Author   : 韩顺平

# 没有使用继承前的代码

# 小学生类
class Pupil:
    name = None
    age = None
    __score = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"name={self.name} age={self.age} score={self.__score}")

    def set_score(self, score):
        self.__score = score

    def testing(self):
        print("..小学生在考小学数学...")


# 大学生类
class Graduate:
    name = None
    age = None
    __score = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"name={self.name} age={self.age} score={self.__score}")

    def set_score(self, score):
        self.__score = score

    def testing(self):
        print(f"..大学生在考高等数学...")


# 测试
student1 = Pupil("apple", 10)
student1.testing()
student1.set_score(70)
student1.show_info()

print("--------------------")
student2 = Graduate("grape", 22)
student2.testing()
student2.set_score(80)
student2.show_info()

# 老韩分析问题
# 1. Pupil 和  Graduate 有很多相同的属性和方法
# 2. 目前这样的做法, 代码复用性差
# 3. 同时也不利于代码的维护和管理
