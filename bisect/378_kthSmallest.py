# https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/
from util.common_imports import *


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l = matrix[0][0]
        r = matrix[n - 1][n - 1]

        while l < r:
            mid = (r + l) // 2
            num = 0  # number of elements <= mid
            j = 0
            for i in range(n - 1, -1, -1):
                while j < n:
                    if matrix[i][j] > mid: # 找到第1 > mid，左边共有j个满足条件 <= mid
                        break
                    j += 1
                num += j

            if num >= k:
                r = mid
            else:
                l = mid + 1
        return l


print(Solution().kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8))

