# https://leetcode-cn.com/problems/diagonal-traverse-ii/
nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]

max_w = 0
for i in range(len(nums)):
    max_w = max(max_w, len(nums[i]))

max_w = max(max_w, len(nums))

res = []
for i in range(max_w * max_w):
    for x in range(min(i, len(nums)-1), -1, -1):
        y = i - x
        if y < len(nums[x]):
            res.append(nums[x][y])

# return res
print (res)

# 超出时间限制