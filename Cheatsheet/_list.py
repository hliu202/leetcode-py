a = [3, 2, 1, 4, 5]

# copy
b = a.copy()
b.append(6)
print(b)

a = [3]
print(a[1:]) # []

# sublist
print(a[0:2])
print(a[1:2]) # [2] 到 index=2 为止(不包含)

# 倒转列表
print(a[::-1])
# 倒转 index
for i in range(len(a) - 1, -1, -1):
    print(i)
for i in reversed(a): # reversed 函数返回一个反转的迭代器。可以是 tuple, string, list 或 range。
    print(i)

# 排序
a.sort(reverse=True)
print(a)

# extend
a = [1, 2]
b = [3, 4]
a.extend(b)
a += b # 1,2,3,4,3,4
print(a)

# range
a = list(range(3, -1, -1))
print(a)  # [3, 2, 1, 0]

# 插入 insert
a = [0, 1, 2, 3]
a.insert(4, 4)
a.insert(0, -1)
print(a)

# bisect 二分法
import bisect
a = []
idx = bisect.bisect_left(a, 3)
a.insert(idx, 3)
idx = bisect.bisect_left(a, 2)
a.insert(idx, 2)
idx = bisect.bisect_left(a, 4)
a.insert(idx, 4)
print(a)
print(bisect.bisect_left(a, 3))
print(bisect.bisect_right(a, 3))
# a.insert(idx, 4)