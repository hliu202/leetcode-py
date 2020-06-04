# https://leetcode-cn.com/problems/product-of-array-except-self/

# left,right 0-i 和 i-len 的乘积
class Solution:
    def productExceptSelf(self, nums):
        leftP, rightP = [0] * len(nums), [0] * len(nums)
        leftP[0] = nums[0]
        rightP[-1] = nums[-1]
        for i in range(1, len(nums)):
            leftP[i] = leftP[i-1] * nums[i]
        for i in range(len(nums) - 2, 0, -1):
            rightP[i] = rightP[i+1] * nums[i]
        res = [0] * len(nums)
        res[0] = rightP[1]
        res[-1] = leftP[-2]
        for i in range(1, len(nums)-1):
            res[i] = leftP[i-1] * rightP[i+1]
        return res

print(Solution().productExceptSelf([1,2,3,4]))
