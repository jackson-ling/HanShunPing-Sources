# @Version  : 1.0
# @Author   : 韩顺平

# 字符串使用注意事项

# 使用引号( ' 或 " ) 包括起来, 创建字符串
str1 = 'tom说: "hello"'
print(str1)
str2 = "jack说: 'hi'"
print(str2)

print(f"str2的类型:{type(str2)}")

# 通过加号可以连接字符串
print("hi" + " tom")

# Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用
str3 = 'A'
print("str3类型", type(str3))

# 用三个单引号'''内容''', 或三个双引号"""内容"""可以使字符串内容保持原样输出,
# 在输出格式复杂的内容是比较有用的, 比如输出一段代码

content = '''be the cat's whiskers/pyjamas " ''

(informal) 最棒的东西（或主意、人等）
to be the best thing, person, idea, etc. " 

He thinks he's the cat's whiskers (= he has a high opinion of himself) .
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
他自以为了不起'''

print(content)

# 在字符串前面加 'r' 可以使整个字符串不会被转义
str4 = r"jack\ntom\tking"
print(str4)

# 讲解字符串的驻留机制
str1 = "Hello"
str2 = "Hello"
str3 = "Hello"

# id()函数是，可以返回对象/数据的内存地址
print("str1的地址:", id(str1))
print("str2的地址:", id(str2))
print("str3的地址:", id(str3))

str1 = "abc123#"
str2 = "abc123#"
print(id(str1), id(str2))

num1 = -100
num2 = -101
print("----------")
print(id(num1), id(num2))


