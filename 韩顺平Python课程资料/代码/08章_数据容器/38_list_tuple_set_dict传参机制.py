# @Version  : 1.0
# @Author   : 韩顺平

"""
    list_tuple_set_dict传参机制
"""


# ------------------------list-----------------------
def f1(my_list):
    print(f"②f1() my_list: {my_list} 地址是: {id(my_list)}")
    my_list[0] = "jack"
    print(f"③f1() my_list: {my_list} 地址是: {id(my_list)}")


# 测试
my_list = ["tom", "mary", "hsp"]
print(f"①my_list: {my_list} 地址是: {id(my_list)}")
# 调用函数
f1(my_list)
print(f"④my_list: {my_list} 地址是: {id(my_list)}")


# ------------------------tuple-----------------------
def f2(my_tuple):
    print(f"②f2() my_tuple: {my_tuple} 地址是: {id(my_tuple)}")
    # 不能修改
    # my_tuple[0] = "red"
    print(f"③f2() my_tuple: {my_tuple} 地址是: {id(my_tuple)}")


# 测试
my_tuple = ("hi", "ok", "hello")
print(f"①my_tuple: {my_tuple} 地址是: {id(my_tuple)}")
f2(my_tuple)
print(f"④my_tuple: {my_tuple} 地址是: {id(my_tuple)}")


# ------------------------set-----------------------
def f3(my_set):
    print(f"②f3() my_set: {my_set} 地址是: {id(my_set)}")  # {"水浒", "西游", "三国"},0x1122
    my_set.add("<<红楼梦>>")
    print(f"③f3() my_set: {my_set} 地址是: {id(my_set)}")  # {"水浒", "西游", "三国",<<红楼梦>>} 0x1122


# 测试
my_set = {"水浒", "西游", "三国"}
print(f"①my_set: {my_set} 地址是: {id(my_set)}")  # {"水浒", "西游", "三国"}，ox1122
f3(my_set)
print(f"④my_set: {my_set} 地址是: {id(my_set)}")  # {"水浒", "西游", "三国",<<红楼梦>>} 0x1122


# ------------------------dict-----------------------
def f4(my_dict):
    print(f"②f4() my_dict: {my_dict} 地址是: {id(my_dict)}")  # {"name": "小倩", "age": 18},0x1122
    my_dict['address'] = "兰若寺"
    print(f"③f4() my_dict: {my_dict} 地址是: {id(my_dict)}")  # {"name": "小倩", "age": 18,"address":"兰若寺" },ox1122


# 测试
my_dict = {"name": "小倩", "age": 18}
print(f"①my_dict: {my_dict} 地址是: {id(my_dict)}")  # {"name": "小倩", "age": 18}, 0x1122
f4(my_dict)
print(f"④my_dict: {my_dict} 地址是: {id(my_dict)}")  # {"name": "小倩", "age": 18,"address":"兰若寺" },ox1122
