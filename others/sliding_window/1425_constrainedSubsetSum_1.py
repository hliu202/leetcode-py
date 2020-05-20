# https://leetcode-cn.com/problems/constrained-subsequence-sum/

# Use dynamic programming.
# Let dp[i] be the solution for the prefix of the array that ends at index i, if the element at index i is in the subsequence.
# dp[i] = nums[i] + max(0, dp[i-k], dp[i-k+1], ..., dp[i-1])
# Use a heap with the sliding window technique to optimize the dp.
from collections import deque

nums = [-1,-2,-3] # [10,2,-10,5,20] # [10,-2,-10,-5,20]
k = 2

dp = deque()
dp.append((nums[0], 0)) # dp[i] and index
res = nums[0]

for i in range(1, len(nums)):
    cur = nums[i]
    for j in range(len(dp)):
        cur = max(cur, dp[j][0] + nums[i])

    while dp and dp[-1][0] < cur:
        dp.pop()
    
    dp.append((cur, i))
    
    if dp[0][1] == i - k:
        res = max(dp.popleft()[0], res)

res = max(res, dp[0][0])
print (res)
