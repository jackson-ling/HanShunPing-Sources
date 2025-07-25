# @Version  : 1.0
# @Author   : 韩顺平

def f2(num):
    res = 0
    for i in range(1, num + 1):
        res += i
    return res


def f1(name):
    print(f"name={name} 1")
    print(f"name={name} 2")
    print(f"name={name} 3")
    print(f"name={name} 4")
    print(f"name={name} 5")
    r = f2(6)
    print(f"r={r}")
    print(f"name={name} 6")
    print(f"name={name} 7")
    print(f"name={name} 8")


f1("韩顺平")
print("end....")
