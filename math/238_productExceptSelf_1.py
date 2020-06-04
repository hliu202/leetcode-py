class Solution:
    def productExceptSelf(self, nums):
        L,R=[0] * len(nums), [0] * len(nums) # i左边和右边的乘积
        L[0] = 1
        for i in range(1, len(nums)):
            L[i] = L[i-1] * nums[i-1]
        R[-1] = 1
        for i in range(len(nums)-2, -1, -1):
            R[i] = R[i+1] * nums[i+1]
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = L[i] * R[i]
        
        return res

print (Solution().productExceptSelf([1,2,3,4]))