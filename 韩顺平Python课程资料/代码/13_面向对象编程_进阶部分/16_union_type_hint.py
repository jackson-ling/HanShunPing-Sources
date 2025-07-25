# @Version  : 1.0
# @Author   : 韩顺平
# 如果要使用Union类型注解, 则需要导入Union
from typing import Union

# 联合类型注解, a 可以是int或者str
a: Union[int, str] = 100

# my_list是list类型, 元素可以是int或者str

my_list: list[Union[int, str]] = [100, 200, 300, "tim"]


# 函数/方法使用联合类型注解
# 接收两个数(可以是int/float), 返回数(int/float)
def cal(num1: Union[int, float],
        num2: Union[int, float]) -> Union[int, float]:
    return float(num1 + num2)


print(f"结果是: {cal(10, 20.2)}")
