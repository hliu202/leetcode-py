# https://leetcode-cn.com/problems/best-sightseeing-pair/

# A[i] + A[j] + i - j = (A[i] + i) + (A[j] - j) # i > j

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        mx = A[0]
        ans = 0
        for i in range(1, len(A)):
             cur = mx + A[i] - i
             ans = max(ans, cur)
             mx = max(mx, A[i] + i)
        return ans