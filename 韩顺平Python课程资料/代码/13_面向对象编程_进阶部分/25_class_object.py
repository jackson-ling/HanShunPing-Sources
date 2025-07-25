# @Version  : 1.0
# @Author   : 韩顺平

class Monster:
    name = "蝎子精"
    age = 300

    def hi(self):
        print(f'hi() {self.name}-{self.age}')


# 下一个断点, 可以看到 Monster的情况
print(Monster)
# 通过Class对象, 可以引用属性 (没有创建实例对象也可以引用/访问)
print(f"Monster.name: {Monster.name} Monster.age:{Monster.age}") #蝎子精 300

# 通过类名如何调用非静态成员方法
Monster.hi(Monster)

print("*" * 32)
