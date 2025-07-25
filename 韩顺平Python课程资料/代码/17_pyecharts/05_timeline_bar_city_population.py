# @Version  : 1.0
# @Author   : 韩顺平


from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

"""准备数据"""

# 确定需要创建多少个Bar对象，根据文件提供的年份 2003-2022
with open("分省年度数据.csv", "r", encoding="gbk") as f:
    data_lines = f.readlines()

# 删除data_lines列表的前3个元素(行)
for _ in range(3):
    data_lines.pop(0)

# 删除data_lines列表的后2个元素(行)
for _ in range(2):
    data_lines.pop(-1)

# print("data_lines", data_lines)
years = data_lines.pop(0).replace("\n", "").split(",")
# 去掉第一个元素"地区"
years.pop(0)

# 遍历 data_lines 生成我们需要的数据
# 难度-需求我们设计一下
# 把数据放到一个字典对象中 data_dict = {年份:[[省市名,人口数],[省市名,人口数]...],年份:[[省市名,人口数],[省市名,人口数]...]...}
# 看一个具体的案例: {2003:[["北京市",1456],["天津市",1011]..],2004:[["北京市",1493],["天津市",1024]..]..}

# 创建字典对象
data_dict = {}

for data_line in data_lines:
    # print("data_line", data_line)
    data_line_list = data_line.replace("\n", "").split(",")
    # 遍历years 给各个城市的各个年份的人口数据添加到data_dict
    index = 0
    for year in years:
        index += 1
        try:
            data_dict[year].append([data_line_list[0], float(data_line_list[index])])
        except Exception as e:
            # 如果出现了异常,说明是第一次添加数据
            data_dict[year] = []
            data_dict[year].append([data_line_list[0], float(data_line_list[index])])

"""创建Timeline对象"""
timeline = Timeline({"theme": ThemeType.ESSOS})
years.reverse()

"""创建Bar对象 并加入到Timeline对象 还有进行配置"""
for year in years:
    # 下面我们需要取出每一年按照人口数量排序的前12省市
    # 1. 先排序 2. 切片
    data_dict[year].sort(key=lambda ele: ele[1], reverse=True)
    rank_12_city_data = data_dict[year][0:12]
    # 定义Bar的X轴数据
    x_data = []
    # 定义Bar的Y轴数据
    y_data = []
    for city in rank_12_city_data:
        x_data.append(city[0])
        y_data.append(city[1])
    # 创建Bar对象
    bar = Bar()
    # 对x_data数据和y_data数据翻转
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("人口(万)", y_data)
    # 转换X和Y轴
    bar.reversal_axis()
    # 全局配置
    bar.set_global_opts(title_opts=opts.TitleOpts(title=f"{year}年中国省市人口排名前12的情况"))

    # 将创建好的bar添加到TimeLine对象
    timeline.add(bar, str(year))

# 对时间线进行配置
timeline.add_schema(
    play_interval=500,
    is_auto_play=True
)

"""生成对应的文件"""

timeline.render("2003-2022年中国省市人口排名前12的情况.html")

# x = Faker.choose()  # ["河马", "蟒蛇", "老虎", "大象", "兔子", "熊猫", "狮子"]
# tl = Timeline()  # 创建Timeline对象
# for i in range(2015, 2020):  # 循环5次,创建了5个Bar柱状图
#     bar = (
#         Bar()
#         .add_xaxis(x)  # 添加X轴数据["河马", "蟒蛇", "老虎", "大象", "兔子", "熊猫", "狮子"]
#         .add_yaxis("商家A", Faker.values())  # [值1,值2....]
#         .add_yaxis("商家B", Faker.values())  # [值1,值2....]
#         .set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))
#     )
#     tl.add(bar, "{}年~~~".format(i))
# tl.render("timeline_bar.html")
