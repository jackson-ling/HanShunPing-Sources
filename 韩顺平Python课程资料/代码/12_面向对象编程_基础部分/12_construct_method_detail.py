# @Version  : 1.0
# @Author   : 韩顺平

# 一个类只有一个  __init__ 方法 , 即使你写了多个, 也只有最后一个生效

class Person:
    name = None
    age = None

    def __init__(self, name, age):
        print(f"__init__ 执行了... 得到了{name} {age}")
        self.name = name
        self.age = age

    def __init__(self, name):
        print(f"__init__ ~~执行了... 得到了{name}")
        self.name = name

# 报错
# p1 = Person("kobe", 20)
# 后面的__init()__ 生效
p1 = Person("kobe")
print(f"p1的 name={p1.name} age={p1.age}") # kobe None


# python可以动态的生成对象属性, 代码说明

class Person:
    name = None
    age = None

    def __init__(self, name, age):
        print(f"__init__ 执行了... 得到了{name} {age}")
        self.name = name
        self.age = age


p1 = Person("kobe", 20)
print(f"p1的 name={p1.name} age={p1.age}")

# 如果p1对象已经有job属性了, 则相等于赋值, 如果没有则相当于创建并赋值
p1.job = "Python工程师"
print(f"p1的 job={p1.job}")


# 老韩说明: 为了代码简洁, 我们也可以通过__init__  动态的生成对象属性
# 构造方法不能有返回值, 比如, 你返回字符串,  会报 "TypeError: __init__() should return None, not 'str'"

class Person:

    def __init__(self, name, age):
        print(f"__init__ 执行了... 得到了{name} {age}")
        # 将接收到的name和age 赋给 当前对象的name和age属性
        # Python支持动态生成对象属性
        self.name = name
        self.age = age


p1 = Person("tim", 30)
print(f"p1的 name={p1.name} age={p1.age}") # tim 30


