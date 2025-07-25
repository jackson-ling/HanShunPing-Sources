# @Version  : 1.0
# @Author   : 韩顺平

# 1) 编写一个Person类，包括属性(name、age), 构造方法、say方法(返回Person自我介绍的字符串）
# 2) 编写一个Student类，继承Person类，增加属性(id、score)，以及构造方法，
# 重写say方法(返回Student自我介绍的信息)
# 3) 分别创建Person和Student对象, 调用say方法输出自我介绍, 体会重写的作用  [文件: override_exercise.py]

# 父类Person
class Person:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return f"名字:{self.name} 年龄:{self.age}"


# 子类Student
class Student(Person):
    id = None
    score = None

    def __init__(self, id, score, name, age):
        # 调用父类的构造器完成继承父类的属性的初始化
        super().__init__(name, age)
        # 子类的特有的属性，我们自己完成初始化
        self.id = id
        self.score = score

    def say(self):
        return f"id:{self.id} 成绩:{self.score} {super().say()}"


# 测试
person = Person("tom", 12)
print(person.say())

student = Student("8-30", 100, "shunping", 20)
print(student.say())
