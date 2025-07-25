# @Version  : 1.0
# @Author   : 韩顺平
from math import fabs

# 导入包下的模块
import hsp_package.module01
import hsp_package.module02

# 使用导入的模块
hsp_package.module01.hi()
hsp_package.module02.ok()


# # from 包名 import 模块 , 这种方式导入, 在使用时, 模块.功能 , 不用带包名
# from hsp_package import module01
#
# # 直接使用模块名.功能名
# module01.hi()


# 导入包的模块的指定函数、类、变量
# from hsp_package.module01 import hi

# 直接使用功能名调用即可
# hi()

# from 包名.模块 import *  : 表示导入包的模块的所有功能
# from hsp_package.module01 import *
#
# hi()
# hello()


# __init__.py 通过 __all__ 控制允许导入的模块

# from hsp_package import *
#
# module02.ok()
# 引入限制了module01模块导入, 因此不能使用
# module01.hi()


# __all__ = ['module02'] 不能限制 下面的导入形式
# import hsp_package.module02
# import hsp_package.module01
#
# hsp_package.module02.ok()
# hsp_package.module01.hi()


# 包可以有多个层级
# 使用方式1， 看起来很麻烦，但是很好理解
# import hsp_package.hsp_package2.module03
#
# hsp_package.hsp_package2.module03.cal(60, 30)


# 使用方式2
# from hsp_package.hsp_package2.module03 import cal

# 直接调用即可
# cal(60, 90)


# 方式3
# from hsp_package.hsp_package2 import module03

# 使用模块名.功能名调用
# module03.cal(90, 10)


print(fabs(-90.8))



