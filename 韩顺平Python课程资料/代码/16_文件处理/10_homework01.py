# @Version  : 1.0
# @Author   : 韩顺平

# 1) 实现登录验证，如果用户名是列表中的元素 ["smith", "tom", "hsp"]  , 密码 "888" 则登录成功 , 否则失败
# 2) 不管登录是否成功, 都需要在文件中记录登录的信息
# 3) 登录成功, 可以看到相应的操作菜单提示, 请实现相应的功能

"""
    思路分析
    1. 根据业务需求, 编写相应的函数
    2. 编写函数operation_menu() 显示操作的菜单
    3. 编写函数record_log() 记录登录信息
    4. 编写函数read_log() 读取登录信息
"""
import time


# 编写函数operation_menu() 显示操作的菜单
def operation_menu():
    print()
    print("请选择操作".center(32, "="))
    print("\t\t\t1 查看当前登录用户")
    print("\t\t\t2 查看登录日志")
    print("\t\t\t3 退出系统")


# 编写函数record_log() 记录登录信息

def record_log(user, info):
    """
    记录登录信息
    :param user: 当前登录用户名
    :param info: 登录成功还是失败的信息
    :return:
    """
    with open("log.txt", mode="a", encoding="utf-8") as f:
        # 构建写入的登录信息
        s = f"登录用户: {user}, {info} 登录时间: {time.strftime("%m-%d %H:%M:%S", time.localtime(time.time()))}\n"
        f.write(s)


# 编写函数read_log() 读取登录信息
def read_log():
    with open("log.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")


# 测试
if __name__ == "__main__":
    user = input("请输入用户名: ")
    pwd = input("请输入密码: ")
    if user in ["smith", "tom", "hsp"] and pwd == "888":
        # 记录登录信息
        record_log(user, "登录成功")
        while True:
            operation_menu()
            key = input("请输入你的选择: ")
            if key == "1":
                print(f"当前登录用户: {user}")
            elif key == "2":
                read_log()
            elif key == "3":
                print("退出系统...")
                break
            else:
                print("你的选择有误, 请重新选择..")
    else:
        record_log(user, "登录失败")
        print("用户名/密码有误, 重新登录")
