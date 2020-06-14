# https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target/

from util.common_imports import *


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        sum_le = 0
        res = arr[-1]  # max
        res_abs = abs(target - n * res)
        for i in range(n):
            cur = arr[i]
            curN = n - i
            curT = target - sum_le
            # less equal cur:
            need = curT // curN
            needCeil = (curT + curN - 1) // curN

            if i > 0 and need <= arr[i-1] and needCeil <= arr[i-1]:
                sum_le += cur
                continue

            if need <= cur:
                sum1 = sum_le + need * curN
                if abs(target - sum1) < res_abs:
                    res = need
                    res_abs = abs(target - sum1)

            if needCeil > need and needCeil <= cur:
                sum2 = sum_le + needCeil * curN
                if abs(target - sum2) < res_abs:
                    res = needCeil
                    res_abs = abs(target - sum2)

            sum_le += cur
        return res

# print(Solution().findBestValue(arr=[4, 9, 3], target=10))
# print(Solution().findBestValue(arr=[2, 3, 5], target=10))
print(Solution().findBestValue(arr=[60864, 25176, 27249, 21296, 20204], target=56803))

