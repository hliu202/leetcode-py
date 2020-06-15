
# 1. 按第 n 个排列
data = [[7,2,3], [4,5,6], [1,8,9]]

sorted_by_second = sorted(data, key=lambda tup: tup[1])
print (sorted_by_second)

data = [(7,2,3), (4,5,6), (1,8,9)]

sorted_by_second = sorted(data, key=lambda tup: tup[1])
print (sorted_by_second)

# 倒序
sorted_by_second = sorted(data, key=lambda tup: tup[1], reverse=True)
print (sorted_by_second)
