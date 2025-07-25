# @Version  : 1.0
# @Author   : 韩顺平

class Demo:
    i = 100

    def m(self):
        self.i += 1
        j = self.i
        print("i=", self.i)  # i= 101
        print("j=", j)  # j= 101


d1 = Demo()
d2 = d1
d2.m()
print(d1.i)  # 101
print(d2.i)  # 101
