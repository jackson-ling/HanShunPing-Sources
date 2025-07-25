# @Version  : 1.0
# @Author   : 韩顺平

# 定义一个元组, ('大话西游', '周星驰', 80, ['周星驰', '小甜甜']),
#  信息为(片名, 导演, 票价, 演员列表))
#
#
# 1) 查询票价对应索引
# 2) 遍历所有的演员
# 3) 删除'小甜甜', 增加演员'牛魔王'、'猪八戒'

tuple_movie = ('大话西游', '周星驰', 80, ['周星驰', '小甜甜'])
# 1) 查询票价对应索引
print(f"票价对应索引 {tuple_movie.index(80)}")  # 2
# 2) 遍历所有的演员
for ele in tuple_movie[3]:
    print(f"演员的名字: {ele}")

# 3) 删除'小甜甜', 增加演员'牛魔王'、'猪八戒'
del tuple_movie[3][1]
tuple_movie[3].append('牛魔王')
tuple_movie[3].append('猪八戒')
print("------------------------")
for ele in tuple_movie[3]:
    print(f"演员的名字: {ele}")



