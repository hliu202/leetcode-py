#  https://leetcode-cn.com/problems/two-sum/

nums = [2,7,11,15]
target = 9

hm = {}
for i in range(len(nums)):
    v = nums[i]
    if target - v in hm:
        print ([hm.get(target - v), i])
        break
    hm[v] = i

# 29/29 cases passed (56 ms)
# Your runtime beats 67.93 % of python3 submissions
# Your memory usage beats 5.48 % of python3 submissions (15.1 MB)
