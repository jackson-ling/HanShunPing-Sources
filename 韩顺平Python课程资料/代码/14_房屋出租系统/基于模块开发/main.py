# @Version  : 1.0
# @Author   : 韩顺平
"""
    说明：出租系统的主程序
"""

# 导入模块house_operation
from house_operation import *


def main():
    """
    这是主函数，也就是程序的执行入口
    :return:
    """
    # 调用main_menu函数显示主菜单
    # 循环显示菜单
    while True:
        main_menu()
        key = input("请输入你的选择(1-6): ")
        if key in ["1", "2", "3", "4", "5", "6"]:
            if key == "1":
                add_house()
            elif key == "2":
                find_house()
            elif key == "3":
                del_house()
            elif key == "4":
                update()
            elif key == "5":
                list_houses()
            elif key == "6":
                if exit_sys():
                    break


# 测试
if __name__ == "__main__":
    main()
    print("你退出了程序,欢迎下次使用...")
