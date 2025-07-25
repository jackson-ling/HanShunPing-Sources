# @Version  : 1.0
# @Author   : 韩顺平

# 它会终结最近的外层循环, 如果循环有可选的 else 子句, 也会跳过该子句
count = 0
while True:
    print("hi while")
    count += 1
    if count == 3:
        break
    while True:
        print("OK while")
        break
else:
    print("Hello, while")

# 如果一个for 循环被 break 所终结, 该循环的控制变量会保持其当前值
nums = [1, 2, 3, 4, 5, 6]
for i in nums:
    if i > 3:
        break

print("i=", i)
