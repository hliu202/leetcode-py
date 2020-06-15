
a = [3,2,1,4,5]

# 倒转列表
print (a[::-1])
# 倒转 index
for i in range(len(a)-1,-1,-1):
    print (i)

# 排序
a.sort(reverse=True)
print (a)