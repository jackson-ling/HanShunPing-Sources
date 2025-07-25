# @Version  : 1.0
# @Author   : 韩顺平

class Clerk:
    # 公共属性
    name = None
    # 私有属性
    __job = None
    __salary = None

    # 构造方法
    def __init__(self, name, job, salary):
        self.name = name
        self.__salary = salary
        self.__job = job

    def get_job(self):
        return self.__job


# 创建对象
clerk = Clerk("apple", "Python工程师", 20000)

# 如果这样使用, 因为Python语言的动态特性, 会动态的创建属性 __job, 但是这个属性
# 和我们在类中定义的私有属性 __job 并不是同一个变量, 我们在类中定义的__job 私有属性完整的名字是 _Clerk__job
# 这里老师使用Debug 来观察，就非常的清楚

clerk.__job = "Go工程师"
print(f"job={clerk.__job}")  # Go工程师
print("ok")

# 获取真正的私有属性__job
print(f"{clerk.get_job()}")  # Python工程师
