from util.common_imports import *

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        D = defaultdict(list)
        n = len(bloomDay)
        Mark = [False] * n
        for i,v in enumerate(bloomDay):
            D[v].append(i)

        days = list(D.keys())
        days.sort()

        cur = 0
        for day in days:
            indices = D[day]
            for idx in indices:
                Mark[idx] = True
                R,L = idx-1, idx+1 # 左右not mark idx
                while R >= 0 and Mark[R]:
                    R -= 1

                if (idx - R) % k == 0:
                    cur += 1
                    if cur == m:
                        return day
                    continue

                while L < n and Mark[L]:
                    L += 1

                if (L-idx) % k == 0:
                    cur += 1
                    if cur == m:
                        return day
                    continue

                if ((L-R - 1)//k) > ((idx - R) // k + (L -idx) // k):
                    cur += 1
                    if cur == m:
                        return day
        return -1

# print(Solution().minDays(bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2))
# print(Solution().minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3))
# print(Solution().minDays(bloomDay = [1,10,3,10,2], m = 3, k = 2))
# print(Solution().minDays(bloomDay = [1000000000,1000000000], m = 1, k = 1))
# print(Solution().minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1))
# print(Solution().minDays(bloomDay = [30,49,11,66,54,22,2,57,35], m = 3, k = 3))
print(Solution().minDays(bloomDay = [62,75,98,63,47,65,51,87,22,27,73,92,76,44,13,90,100,85], m = 3, k = 3))