

class Solution:
    def maxProduct(self, nums) -> int:
        max0,max1 = 0,0
        for v in nums:
            if v >= max0:
                max1 = max0
                max0 = v
            elif v >= max1:
                max1 = v
        return (max0-1) * (max1-1)

# print(Solution().maxProduct([3,4,5,2]))
# print(Solution().maxProduct([1,5,4,5]))
# print(Solution().maxProduct([3,7]))
print(Solution().maxProduct([10,2,5,2]))