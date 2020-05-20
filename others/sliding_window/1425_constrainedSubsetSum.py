# https://leetcode-cn.com/problems/constrained-subsequence-sum/

# Use dynamic programming.
# Let dp[i] be the solution for the prefix of the array that ends at index i, if the element at index i is in the subsequence.
# dp[i] = nums[i] + max(0, dp[i-k], dp[i-k+1], ..., dp[i-1])

# Use a heap with the sliding window technique to optimize the dp!

nums = [-1, -2, -3, -4 ,-5] # [10,-2,-10,-5,20]
k = 2

dp = []
dp.append(nums[0])

for i in range(1,len(nums)):
    r = nums[i]
    for j in range(1,k+1):
        if i - j >= 0:
            r = max(dp[i-j] + nums[i], r)
        
    dp.append(r)

print (max(dp))

# 超出时间限制，最坏情况下 O(n^2) if k == n
