# @Version  : 1.0
# @Author   : 韩顺平

lst1 = [ele * 2 for ele in range(1, 5)]
print("lst1: ", lst1)  # [2,4,6,8]
lst2 = [ele + ele for ele in "韩顺平"]
print("lst2: ", lst2)  # ['韩韩", "顺顺", "平平"]

# 再举一个案例, 要求生成一个列表, 内容为 [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [1*1, 2*2, 3*3..]
lst3 = [ele * ele for ele in range(1, 11)]
print("lst3: ", lst3)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
