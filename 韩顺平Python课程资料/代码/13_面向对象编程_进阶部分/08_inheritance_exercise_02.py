# @Version  : 1.0
# @Author   : 韩顺平

# 2、编写Computer类，包含CPU、内存、硬盘等属性  5min
# 1) get_details方法用于返回Computer的详细信息
# 2) 编写PC子类，继承Computer类，添加特有属性【品牌brand】
# 3) 编写NotePad子类，继承Computer类，添加特有属性【color】
# 4) 完成测试，创建PC和NotePad对象，分别给对象中特有的属性赋值，
# 以及从Computer类继承的属性赋值，并使用方法打印输出信息 [文件: inheritance_exercise_02.py]

"""
    思路分析
    1. 父类: Computer
    2. 公共属性： CPU(cpu)、内存(memory)、硬盘(disk)
    3. 构造器: __init__(self, cpu,memory, disk)
    4. 方法: get_details(self)
    5. 子类: PC(Computer)
    6. 公共属性: brand
    7. 构造器： __init__(self, cpu,memory, disk,brand), 有一个新的知识点
    8. 方法: print_info(self) 完成功能: 输出pc对象的信息(即属性的信息)
"""


class Computer:
    cpu = None
    memory = None
    disk = None

    def __init__(self, cpu, memory, disk):
        self.cpu = cpu
        self.disk = disk
        self.memory = memory

    def get_details(self):
        return f"cpu:{self.cpu}\t内存:{self.memory}\t硬盘:{self.disk}"


class PC(Computer):
    brand = None

    def __init__(self, cpu, memory, disk, brand):
        # 初始化子类的属性-方式1
        # self.cpu = cpu
        # self.memory = memory
        # self.disk = disk
        # self.brand = brand
        # 初始化子类的属性-方式2
        """
            老师解读
            1. 通过super().xx 方式可以去调用父类的方法, 注意关于 super() 后面还有细节会讲到
            2. 这里，我们就通过super().__init__(cpu, memory, disk) 去调用父类的构造器
               完成对父类属性的初始化任务
            3. self.brand = brand 表示子类特有属性，由子类的构造器完成初始化
        """
        super().__init__(cpu, memory, disk)
        self.brand = brand


    def print_info(self):
        """
        完成打印当前对象的信息
        :return:
        """
        print(f"品牌:{self.brand}\t{self.get_details()}")


# 测试
pc = PC("intel", 32, 1000, "戴尔")
pc.print_info()
