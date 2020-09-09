# 初始化，子集
a = [0, 1, 2]
Sa = set(a)
Sb = {0, 1}
print(Sb.issubset(Sa))

# add，update
Sb.add(3)
Sa.update(Sb)
print(Sa)

# 去重
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
nl = list(set(test_list))
print(nl)
