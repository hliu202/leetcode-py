
class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        M = max(candies)
        res = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= M:
                res[i] = True
        
        return res

print(Solution().kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))
print(Solution().kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1))
print(Solution().kidsWithCandies(candies = [12,1,12], extraCandies = 10))