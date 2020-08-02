from util.common_imports import *

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if abs(arr[j] - arr[i]) <= a:
                    for k in range(j + 1, n):
                        if abs(arr[k] - arr[j]) <= b and abs(arr[i] - arr[k]) <= c:
                            ans += 1
        return ans
print(Solution().countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3))
print(Solution().countGoodTriplets(arr = [1,1,2,2,3], a = 0, b = 0, c = 1))
