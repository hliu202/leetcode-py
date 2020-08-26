# 初始化，子集
a = [0, 1, 2]
Sa = set(a)
Sb = {0, 1}
print(Sb.issubset(Sa))

# add，update
Sb.add(3)
Sa.update(Sb)
print(Sa)

