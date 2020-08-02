from util.common_imports import *

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        n = len(grid)

        dq = deque()
        for i in range(n):
            c0 = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    c0 += 1
                else:
                    break
            dq.append(n - c0 - 1) # from 0 to n-1
        
        ans = 0
        for i in range(n): # 选择最近的满足条件的第 n 行
            for j in range(i, n):
                if dq[j] <= i:
                    ans += j - i
                    del dq[j]
                    dq.appendleft(0)
                    break
                else:
                    if j == n - 1:
                        return -1
        return ans

print(Solution().minSwaps(grid = [[0,0,1],[1,1,0],[1,0,0]]))
print(Solution().minSwaps([[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]))
print(Solution().minSwaps(grid = [[1,0,0],[1,1,0],[1,1,1]]))