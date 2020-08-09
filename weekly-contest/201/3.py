from util.common_imports import *


# class Solution:
#     def maxNonOverlapping(self, nums: List[int], target: int) -> int:
#         pre = set()
#         ans = 0
#         for i in range(len(nums)):
#             if target - nums[i] in pre:
#                 ans += 1
#                 pre = set()
#             elif nums[i] == target:
#                 ans += 1
#                 pre = set()
#             else:
#                 tmp = set()
#                 for p in pre:
#                     tmp.add(p + nums[i])
#                 pre = tmp
#                 pre.add(nums[i])
#         return ans


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        sums = []
        positive = []
        ans = 0
        start = 0
        for i in range(len(nums)):
            if nums[i] == target:
                ans += 1
                sums, positive = [], []
            else:
                for j in range(len(sums)):
                    sums[j] += nums[i]
                if i > start:
                    if not (
                        (nums[i - 1] > 0 and nums[i] > 0)
                        or (nums[i - 1] < 0 and nums[i] < 0)
                    ):
                        positive.append(i)
                        sums.append(nums[i])
                else:
                    positive.append(i)
                    sums.append(nums[i])

                for j in range(len(sums)):
                    if sums[j] == target:
                        sums, positive = [], []
                        start = i + 1
                        ans += 1
                        break
                    if nums[positive[j]] >= 0:
                        if sums[j] > target:
                            end = i if (j == len(sums) - 1) else positive[j + 1]
                            SUM = sums[j]
                            for k in range(positive[j], end):
                                SUM -= nums[k]
                                if SUM == target:
                                    ans += 1
                                    sums, positive = [], []
                                    start = i + 1
                                    break
                                elif SUM < target:
                                    break
                        # sums[j] < target and positive
                    else:
                        if sums[j] < target:
                            end = i if (j == len(sums) - 1) else positive[j + 1]
                            SUM = sums[j]
                            for k in range(positive[j], end):
                                SUM -= nums[k]
                                if SUM == target:
                                    ans += 1
                                    sums, positive = [], []
                                    start = i + 1
                                    break
                                elif SUM > target:
                                    break
        return ans


# print(Solution().maxNonOverlapping(nums=[1, 1, 1, 1, 1], target=2))
# print(Solution().maxNonOverlapping(nums=[-1, 3, 5, 1, 4, 2, -9], target=6))
# print(Solution().maxNonOverlapping(nums=[-2, 6, 6, 3, 5, 4, 1, 2, 8], target=10))
# print(Solution().maxNonOverlapping(nums=[0, 0, 0], target=0))
# print(Solution().maxNonOverlapping(nums=[1,2,3,4], target=8))
print(Solution().maxNonOverlapping(nums=[-1,-2,8,-3,8,-5,5,-4,5,4,1], target=5)) # 边界条件?
# 超时 2,1,2, ...: 20000

