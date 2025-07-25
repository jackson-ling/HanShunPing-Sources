# @Version  : 1.0
# @Author   : 韩顺平

class GrandPa:
    name = "大头爷爷"
    hobby = "旅游"


class Father(GrandPa):
    name = "大头爸爸"
    age = 39


class Son(Father):
    name = "大头儿子"


son = Son()

print(f"son.name={son.name} son.age={son.age} son.hobby={son.hobby}")  # 大头儿子 39  旅游
