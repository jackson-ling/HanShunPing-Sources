# @Version  : 1.0
# @Author   : 韩顺平
"""
    说明： 业务层: 提供对房屋操作方法
"""

from house import *


class HouseService:
    # 定义属性houses列表,存放房屋信息(对象)
    houses = []
    # 定义属性id_counter: 记录当前房屋的id
    id_counter = 1

    def find_by_id(self, find_id):
        """
        根据find_id返回对应的house对象,不存在返回None
        :param find_id:
        :return:
        """
        # 遍历houses
        for house in self.houses:
            if find_id == house.id:
                return house

    def del_by_id(self, del_id):
        """
        根据接收到的id删除房屋
        :param del_id:
        :return: 如果删除成功返回True,否则返回false
        """
        # 判断del_id是否存在
        house = self.find_by_id(del_id)
        if house is None:
            return False

        # 如果找到该house,就删除
        self.houses.remove(house)
        return True

    def add(self, new_house: House):
        """
        将接收到的new_house添加到houses
        :param new_house:
        :return:
        """
        # 分配id给new_house
        self.id_counter += 1
        new_house.id = self.id_counter
        self.houses.append(new_house)

    def __init__(self):
        # 为了测试方便,我们在houses列表中增加一个测试数据
        house = House(1, "tim", "118", "海淀", 800, "未出租")
        self.houses.append(house)

    def get_houses(self):
        """
        返回房屋列表
        :return:
        """
        return self.houses
