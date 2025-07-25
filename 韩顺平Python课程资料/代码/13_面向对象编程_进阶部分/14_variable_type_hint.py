# @Version  : 1.0
# @Author   : 韩顺平

# 基础数据类型注解
"""
    老韩解读:
    1. n1: int: 对n1进行类型注解, 标注n1的类型为int
    2. 注意如果，给出的值的类型和标注的类型不一致,则PyCharm会给出黄色警告
"""
n1: int = 10
n2: float = 10.1
is_pass: bool = True
name: str = "燕赤霞"


# 定义类Cat
class Cat:
    pass


# 实例对象类型注解
# cat: Cat: 对cat进行类型注解, 标注cat的类型是Cat
cat: Cat = Cat()

# 容器类型注解
"""
    老韩解读
    1. my_list: list  对my_list进行类型注解, 标注my_list类型为list
    2. ...
"""
my_list: list = [100, 200, 300]
my_tuple: tuple = ("run", "sing", "fly")
my_set: set = {"jack", "tim", "hsp"}
my_dict: dict = {"no1": "北京", "no2": "上海"}

# 容器详细类型注解
"""
    my_list2: list[int]
    对 my_list2进行类型注解: 标注 my_list2类型是list,而且该list元素是int..
"""
my_list2: list[int] = [100, 200, 300]
# 元组类型设置详细类型注解, 需要把每个元素类型都标注一下
my_tuple2: tuple[str, str, str, float] = ("run", "sing", "fly", 1.1)
my_set2: set[str] = {"jack", "tim", "hsp"}
# 字典类型设置详细类型注解, 需要设置两个类型, 即[key类型, value类型]
# my_dict2: dict[str, int]: 对my_dict2进行类型注解, 标注my_dict2类型是dict, 而且
# key的类型是str, values的类型是int
my_dict2: dict[str, int] = {"no1": 100, "no2": 200}

# 注释中使用注解
# 老韩解读 # type: float 用于标注 变量n3 的类型是 float
n3 = 89.9  # type: float
my_list3 = [100, 200, 300]  # type: list[int]
email = "hsp@sohu.com"  # type: str
