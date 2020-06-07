class Solution:
    def shuffle(self, nums, n: int):
        res = [0] * 2 * n
        for i in range(n):
            res[2*i] = nums[i]
            res[2*i+1] = nums[n+i]
        return res

print(Solution().shuffle(nums = [1,2,3,4,4,3,2,1], n = 4))
print(Solution().shuffle(nums = [1,1,2,2], n = 2))