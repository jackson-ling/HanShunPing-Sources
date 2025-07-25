# @Version  : 1.0
# @Author   : 韩顺平

# 演示集合常用操作
# 定义集合
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# 1  len(集合): 集合元素个数
print("basket的元素个数:", len(basket))  # 4
# 2  x in s: 检测 x 是否为 s 中的成员
# 需求: 判断apple是否在集合中
print("apple" in basket)  # T

# 3  add(elem): 将元素 elem 添加到集合中
# 需求: 将grape添加到集合中
basket.add("grape")
print("basket的元素:", basket)  # {'grape', 'orange', 'apple', 'pear', 'banana'}

# 4  remove(elem) ： 从集合中移除元素 elem。
# 如果 elem 不存在于集合中则会引发 KeyError
# 需求: 将 apple从集合删除
basket.remove("apple")
print("basket的元素:", basket)  # {'banana', 'grape', 'orange', 'pear'}

# 5  pop()： 从集合中移除并返回任意一个元素。
# 如果集合为空则会引发 KeyError
# 需求: 从集合中随机删除一个元素
ele = basket.pop()
print("ele:", ele, " 类型是:", type(ele))  # ele: ? 类型: str
# 注意pop() 操作会影响到原集合
print("basket的元素:", basket)  # 只有3个元素

# 6  union(*others): 返回一个新集合，
# 其中包含来自原集合以及 others 指定的所有集合中的元素
# 示意图说明一下
books = {'天龙八部', '笑傲江湖'}
books_2 = {'雪山飞狐', '神雕侠侣', '天龙八部'}
# 需求: 将books 和 books_2 进行合集操作 [即：求出在books集合或者在books_2集合的元素]
books_3 = books.union(books_2)
# books_3 = books | books_2
print("books_3:", books_3)  # {'天龙八部', '笑傲江湖', '雪山飞狐', '神雕侠侣'}

# 7  intersection(*others): 返回一个新集合，
# 其中包含原集合以及 others 指定的所有集合中共有的元素
# 需求: 对 books 和 books_2 求交集 [即:求出既在books又在books_2集合的元素]
books_4 = books.intersection(books_2)
# books_4 = books & books_2
print("books_4->", books_4)  # {'天龙八部'}

# 8  difference(*others): 返回一个新集合，
# 其中包含原集合中在 others 指定的其他集合中不存在的元素
# 也就是：set - other - ...

books = {'天龙八部', '笑傲江湖'}
books_2 = {'雪山飞狐', '神雕侠侣', '天龙八部'}

# 需求: 求出 只存在books集合的元素
# books_5 = books - books_2
books_5 = books.difference(books_2)
print("books_5:", books_5)  # {'笑傲江湖'}

# 需求：求出只存在books2集合的元素
# books_6 = books_2 - books
books_6 = books_2.difference(books)
print("books_6:", books_6)  # ['雪山飞狐', '神雕侠侣']
