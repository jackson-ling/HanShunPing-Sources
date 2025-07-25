# @Version  : 1.0
# @Author   : 韩顺平
"""
    说明: 界面层, 显示界面，接收用户的输入，调用业务层的方法
"""

from house_service import *
from utility import *


class HouseView:
    # 定义属性house_operation【HouseService】
    house_operation: HouseService = HouseService()

    def update_house(self):
        """
        显示修改的界面，输入新的数据,修改对应的房屋信息即可
        :return:
        """
        update_id = int(input("请选择待修改的房屋编号(-1表示退出): "))
        if update_id == -1:
            print("你放弃修改房屋信息".center(32, "="))
            return
        # 根据id查找对应的房屋信息(对象)
        house = self.house_operation.find_by_id(update_id)
        if not house:
            print("没有要修改的房屋信息".center(32, "="))
            return

        # 因为返回的house是对象,所以修改该对象的属性即可
        house.name = Utility.read_str(f"姓名({house.name}): ", house.name)
        house.phone = Utility.read_str(f"电话({house.phone}): ", house.phone)
        house.address = Utility.read_str(f"地址({house.address}): ", house.address)
        house.rent = int(Utility.read_str(f"租金({house.rent}): ", house.rent))
        house.state = Utility.read_str(f"状态({house.state}): ", house.state)

        print("修改房屋信息成功".center(32, "="))

    def find_house(self):
        """
        显示查找的界面,接收用户输入id，查找并显示房屋信息
        :return:
        """
        print("查找房屋信息".center(32, "="))
        find_id = int(input("请输入要查找的id: "))
        # 调用方法返回对应的房屋
        house = self.house_operation.find_by_id(find_id)
        if house:
            # 打印表头信息
            print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态(未出租/已出租)")
            print(house)
        else:
            print(f"查找房屋信息id {find_id} 不存在")

    def exit_sys(self):
        """
        退出系统(需求确认)
        :return:
        """
        key = Utility.read_confirm_select()
        if key == 'y':
            return True
        else:
            return False

    def del_house(self):
        """
        删除房屋的界面, 接收用户的输入
        :return:
        """
        print("删除房屋信息".center(32, "="))
        del_id = int(input("请输入待删除房屋的编号(-1退出): "))
        if del_id == -1:
            print("放弃删除房屋信息".center(32, "="))
            return

        choice = Utility.read_confirm_select()

        if choice == 'y':  # 如果真的要删除
            # 调用Service层的方法
            if self.house_operation.del_by_id(del_id):

                print("删除房屋信息成功".center(32, "="))
            else:
                print("房屋编号不存在, 删除失败..".center(32, "="))

        else:
            print("放弃删除房屋信息".center(32, "="))

    def add_house(self):
        """
        显示添加的界面,接收用户的输入,构建House对象
        :return:
        """
        print("添加房屋".center(32, "="))
        name = input("姓名: ")
        phone = input("电话: ")
        address = input("地址: ")
        rent = int(input("租金: "))
        state = input("状态: ")

        # 构建房屋对象
        new_house = House(0, name, phone, address, rent, state)
        # 调用service方法,添加new_house
        self.house_operation.add(new_house)
        print("添加房屋成功".center(32, "="))

    def list_houses(self):
        """
        显示房屋列表
        :return:
        """
        print("房屋列表".center(60, "="))
        # 打印表头信息
        print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态(未出租/已出租)")
        # 得到houses列表
        houses = self.house_operation.get_houses()
        # 遍历houses这个列表
        for house in houses:
            print(house)  # 先看看效果

        print("房屋列表显示完毕".center(60, "="))

    def main_menu(self):
        """
        显示主菜单
        :return:
        """
        while True:
            print()
            print("房屋出租系统菜单".center(32, "="))
            print("\t\t\t1 新　增　房　源")
            print("\t\t\t2 查　找　房　屋")
            print("\t\t\t3 删　除　房　屋　信　息")
            print("\t\t\t4 修　改　房　屋　信　息")
            print("\t\t\t5 房　屋　列　表")
            print("\t\t\t6 退　　　　　出")
            key = input("请输入你的选择(1-6): ")
            if key in ["1", "2", "3", "4", "5", "6"]:
                if key == "1":
                    self.add_house()
                elif key == "2":
                    self.find_house()
                elif key == "3":
                    self.del_house()
                elif key == "4":
                    self.update_house()
                elif key == "5":
                    self.list_houses()
                elif key == "6":
                    if self.exit_sys():
                        break
