class Solution:
    def getLastMoment(self, n: int, left, right) -> int:
        max_left = max(left) if left else 0
        r = 0
        if right:
            min_right = min(right)
            r = n - min_right
        return max(max_left, r)

print(Solution().getLastMoment(n = 4, left = [4,3], right = [0,1]))
print(Solution().getLastMoment(n = 7, left = [], right = [0,1,2,3,4,5,6,7]))
print(Solution().getLastMoment(n = 7, left = [0,1,2,3,4,5,6,7], right = []))
print(Solution().getLastMoment(n = 9, left = [5], right = [4]))
print(Solution().getLastMoment(n = 6, left = [6], right = [0]))