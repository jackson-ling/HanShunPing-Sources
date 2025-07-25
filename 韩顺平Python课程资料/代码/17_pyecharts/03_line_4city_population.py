# @Version  : 1.0
# @Author   : 韩顺平

import pyecharts.options as opts
from pyecharts.charts import Line

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.apache.org/examples/editor.html?c=line-simple

目前无法实现的功能:

暂无
"""

# 创建Line对象 折线图对象
line = Line()

# 准备X轴数据
# 打开文件
f = open("分省年度数据.csv", "r", encoding="gbk")
# 为了方便小伙伴理解, 先输出文件的内容
# for line in f:
#     print(line, end="")
# f.close()

# 给X轴添加数据
"""
    分析， 数据就是 [2003, 2004, .... 2022]
"""

# 读取所有的行数据
line_datas = f.readlines()
f.close()

# 先删除前面三个行(元素)
for _ in range(3):
    line_datas.pop(0)

# 得到x轴的数据
# 得到 ['地区', '2022年', '2021年', '2020年', '2019年', '2018年', '2017年', '2016年', '2015年',..]
x_data_year = line_datas.pop(0).replace("\n", "").split(",")
x_data_year.pop(0)  # ['2022年', '2021年',... '2003年']
x_data_year.reverse()  # ['2003年', '2004年', '2005年',... '2022年']
# print(x_data_year)


# 给Y轴添加数据
"""
    分析： 这里有四组数据，分别是 北京 上海 天津, 重庆的近20年的人口数据
"""
# 创建四个列表，存放 北京 上海 天津, 重庆的近20年的人口数据
y_data_bj = []
y_data_sh = []
y_data_tj = []
y_data_cq = []

# 遍历 line_datas 得到 北京 上海 天津, 重庆的近20年的人口数据
for line_data in line_datas:
    line_data = line_data.replace("\n", "").split(",")
    if line_data[0] == "北京市":
        line_data.pop(0)
        line_data.reverse()  # 从2003-2022年的排序
        y_data_bj = line_data
    elif line_data[0] == "上海市":
        line_data.pop(0)
        line_data.reverse()
        y_data_sh = line_data
    elif line_data[0] == "天津市":
        line_data.pop(0)
        line_data.reverse()
        y_data_tj = line_data
    elif line_data[0] == "重庆市":
        line_data.pop(0)
        line_data.reverse()
        y_data_cq = line_data

# 添加X轴的数据
line.add_xaxis(x_data_year)
# 添加Y轴的数据
line.add_yaxis("重庆市历年人口", y_data_cq, label_opts=opts.LabelOpts(is_show=False))
line.add_yaxis("北京市历年人口", y_data_bj, label_opts=opts.LabelOpts(is_show=False))
line.add_yaxis("上海市历年人口", y_data_sh, label_opts=opts.LabelOpts(is_show=False))
line.add_yaxis("天津市历年人口", y_data_tj, label_opts=opts.LabelOpts(is_show=False))

# 设置全局配置项
line.set_global_opts(
    title_opts=opts.TitleOpts(title="2003-2022年直辖市总人口折线图", pos_left="center", pos_bottom="1%"))

# 生成文件
line.render("line_4city_population.html")

# x_data = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# y_data = [820, 932, 901, 934, 1290, 1330, 1320]
# y_data_2 = [8201, 9321, 9011, 9341, 12901, 13301, 13201]
#
#
# (
#     Line()
#     .set_global_opts(
#         tooltip_opts=opts.TooltipOpts(is_show=False),
#         xaxis_opts=opts.AxisOpts(type_="category"),
#         yaxis_opts=opts.AxisOpts(
#             type_="value",
#             axistick_opts=opts.AxisTickOpts(is_show=True),
#             splitline_opts=opts.SplitLineOpts(is_show=True),
#         ),
#     )
#     .add_xaxis(xaxis_data=x_data)
#     .add_yaxis(
#         series_name="",
#         y_axis=y_data,
#         symbol="emptyCircle",
#         is_symbol_show=True,
#         label_opts=opts.LabelOpts(is_show=False),
#     )
#     .add_yaxis(
#         series_name="",
#         y_axis=y_data_2,
#         symbol="emptyCircle",
#         is_symbol_show=True,
#         label_opts=opts.LabelOpts(is_show=False),
#     )
#     .render("basic_line_chart.html")
# )
