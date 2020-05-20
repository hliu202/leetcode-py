# https://leetcode-cn.com/problems/diagonal-traverse-ii/

nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
# idx = list(len(nums))

res = []

for i,r in enumerate(nums):
    for j,a in enumerate(r):
        if len(res) <= i + j:
            res.append([])
        res[i+j].append(a)  # 第 i+j 条斜线上的元素

res2 = []
for r in res:
    res2.extend(r[::-1])    # 逆序添加
# return res2
print (res2)