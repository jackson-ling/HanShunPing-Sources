# @Version  : 1.0
# @Author   : 韩顺平


# 编写Doctor类, 属性:name, age, job, gender, sal,
# 5个参数的构造器，重写 __eq__()方法，
# 并判断测试类中创建的两个对象是否相等(相等就是判断属性是否相同)

class Doctor:
    def __init__(self, name, age, job, gender, sal):
        self.name = name
        self.age = age
        self.job = job
        self.gender = gender
        self.sal = sal

    # 重写__eq__
    def __eq__(self, other):
        # 如果other类型不受Doctor直接返回false
        if not isinstance(other, Doctor):
            return False
        # 如果所有的属性都相同, 则返回True
        return (self.job == other.job and
                self.sal == other.sal and
                self.age == other.age and
                self.gender == other.gender
                and self.name == other.name)


# 测试
doctor1 = Doctor("king", 20, "牙科医生", "男", 10000)
doctor2 = Doctor("king", 20, "牙科医生", "男", 10000)

print("doctor1 == doctor2", doctor1 == doctor2)
