# @Version  : 1.0
# @Author   : 韩顺平

from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

"""准备数据"""
with open("分省年度数据.csv", "r", encoding="gbk") as f:
    data_lines = f.readlines()

# 删除data_lines列表的前4个元素(行)
for _ in range(4):
    data_lines.pop(0)

# 创建一个空的列表存放地图数据
# 分析map_data_list 格式 [[省市名, 人口数量], [省市名, 人口数量]....]
map_data_list = []

for data_line in data_lines:
    data_line_list = data_line.split(",")
    try:
        map_data_list.append([data_line_list[0], data_line_list[1]])
    except Exception as e:
        # 如果在添加数据到map_data_list出现异常,我们就continue
        continue

print("map_data_list", map_data_list)

"""创建Map对象"""
map = Map()

"""添加数据并配置"""
map.add("2022年各省市的人口分布情况", map_data_list, "china")

# 全局配置
map.set_global_opts(
    title_opts=opts.TitleOpts(title="2022年各省市的人口分布情况"),
    # VisualMapOpts：视觉映射配置项
    visualmap_opts=opts.VisualMapOpts(
        # 指定 visualMapPiecewise 组件的最小值。
        min_=100,
        # 指定 visualMapPiecewise 组件的最大值。
        max_=15000,
        # 指定 visualMapPiecewise 组件的位置。
        pos_left="10%",
        pos_bottom="30%"
    )
)

# 系列配置-标签字体大小配置
map.set_series_opts(label_opts=opts.LabelOpts(font_size=8))

"""生成文件"""
map.render("2022年各省市的人口分布情况.html")

# c = (
#     Map()
#     # 解读 add方法 1. "商家A" 数据名称 2. [list(z) for z in zip(Faker.provinces, Faker.values())] 显示标签的值 3. china对应中国地图
#     .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
#     .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"))
#     .render("map_base.html")
# )

# print([list(z) for z in zip(Faker.provinces, Faker.values())])
