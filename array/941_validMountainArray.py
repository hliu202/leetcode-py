from util.common_imports import *


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) <= 2:
            return False

        # !特殊情况，只有递减
        if A[0] > A[1]:
            return False

        cur_incr = True
        for i in range(2, len(A)):
            if A[i - 1] == A[i]:
                return False

            if A[i - 1] < A[i]:
                if cur_incr:
                    continue
                else:
                    return False
            else:
                if cur_incr:
                    cur_incr = False
                    continue
                else:
                    continue

        return not cur_incr


# print(Solution().validMountainArray([2, 1]))
# print(Solution().validMountainArray([3, 5, 5]))
# print(Solution().validMountainArray([0, 3, 2, 1]))
print(Solution().validMountainArray([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))


# !线性扫描
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # 递增扫描
        while i + 1 < N and A[i] < A[i + 1]:
            i += 1

        # !最高点不能是数组的第一个位置或最后一个位置
        if i == 0 or i == N - 1:
            return False

        # 递减扫描
        while i + 1 < N and A[i] > A[i + 1]:
            i += 1

        return i == N - 1
