# @Version  : 1.0
# @Author   : 韩顺平


# 1字典的Key(关键字)通常是字符串或数字, Value可以是任意数据类型

dict_a = {
    "jack": [100, 200, 300],
    "mary": (10, 20, "hello"),
    "nono": {"apple", "pear"},
    "smith": "计算机老师",
    "周星驰": {
        "性别": "男",
        "age": 18,
        "地址": "香港"
    },
    "key1": 100,
    "key2": 9.8,
    "key3": True

}
print(f"dict_a: {dict_a} 类型: {type(dict_a)}")

# 2、字典不支持索引
# print(dict_a[0])

# 3、既然字典不支持索引, 所以对字典进行遍历不支持while , 只支持for

dict_b = {'one': 1, 'two': 2, 'three': 3}
# 遍历方式1-依次取出key, 再通过dict[key]取出对应的value
print("----------遍历方式1----------")
for key in dict_b:
    print(f"key: {key} value: {dict_b[key]}")

# 遍历方式2-依次取出value
print("----------遍历方式2----------")
for value in dict_b.values():
    print(f"value: {value}")

# 遍历方式3-依次取出key-value
print("----------遍历方式3----------")
for k, v in dict_b.items():
    print(f"key:{k} value: {v}")

# 4、创建空字典可以通过{}，或者 dict()
dict_c = {}
dict_d = dict()
print(f"dict_c: {dict_c} 类型: {type(dict_c)}")  # {} dict
print(f"dict_d: {dict_d} 类型: {type(dict_d)}")  # {} dict

# 5、字典的key必须是唯一的, 如果你指定了多个相同的key , 后面的键值对会覆盖前面的
dict_e = {'one': 1, 'two': 2, 'three': 3, 'two': 200}
print(f"dict_e: {dict_e}")  # {'one': 1, 'two': 200, 'three': 3 }
