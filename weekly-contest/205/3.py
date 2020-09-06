from util.common_imports import *
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        n = len(cost)
        i = 0
        ans = 0

        while i < n:
            j = i + 1
            
            while j < n and s[j] == s[i]:
                j += 1

            n_same = j - i
            if n_same > 1:
                total = 0
                max_cost = -1
                for k in range(i, j):
                    total += cost[k]
                    max_cost = max(max_cost, cost[k])

                ans += total - max_cost
            i = j
        return ans

# print(Solution().minCost(s = "abaac", cost = [1,2,3,4,5]))
# print(Solution().minCost(s = "abc", cost = [1,2,3]))
# print(Solution().minCost(s = "aabaa", cost = [1,2,3,4,1]))
print(Solution().minCost(s = "bbbaaa", cost = [4,9,3,8,8,9])) # 23
