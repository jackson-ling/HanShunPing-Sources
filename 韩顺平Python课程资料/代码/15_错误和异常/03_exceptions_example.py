# @Version  : 1.0
# @Author   : 韩顺平


# IndexError: 当序列抽取超出范围时将被引发
# str = "hello,abc" # 9
# print(str[100])

# list_a = ["jack", "tom", "yoyo", "nono", "hsp"]
# print(list_a[5])


# KeyError: 当在现有键集合中找不到指定的映射（字典）键时将被引发
# dict_a = {"name": "jack", "age": 10, "gender": "男"}
# print(dict_a["sex"])


# NameError: 当某个局部或全局名称未找到时将被引发, 比如你使用了一个没有定义的变量名.

# print("nums is:", nums)


# TypeError: 当一个操作或函数使用了, 类型不适当的对象时将被引发
# a = 'hello'
# b = 5
# print(a + b)


# 5、ValueError:  当操作或函数接收到具有正确类型但值不适合的参数 时将被引发

# print(int("123"))  # 对
# print(int("hello"))  # 抛出/触发/引发异常


# 7、FileNotFoundError:  请求的文件或目录不存在时将被引发
# f = open("d://ttt/t.txt", "r")


# 8、AttributeError:  当属性引用或赋值失败时将被引发
class A:
    def hi(self):
        pass

a = A()
print(a.name)