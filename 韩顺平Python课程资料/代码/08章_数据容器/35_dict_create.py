# @Version  : 1.0
# @Author   : 韩顺平

books = ["红楼梦", "三国演义", "西游记", "水浒传"]
authors = ["曹雪芹", "罗贯中", "吴承恩", "施耐庵"]
dict_book = {book: author for book, author in zip(books, authors)}
print("dict_book:", dict_book)

str1 = "韩顺平"
dict_str = {ele1: ele2 * 2 for ele1, ele2 in zip(str1, str1)}
print("dict_str:", dict_str)

english_list = ["red", "black", "yellow", "white"]
chinese_list = ["红色", "黑色", "黄色", "白色"]

dict_color = {ele1: ele2.upper() for ele1, ele2 in zip(chinese_list, english_list)}
print("dict_color:", dict_color)
# 生成一个字典:
# {'红色': 'RED', '黑色': 'BLACK', '黄色': 'YELLOW', '白色': 'WHITE'}
