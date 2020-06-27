# https://leetcode-cn.com/problems/first-missing-positive/submissions/
# Hash 标记，将数组当做hash表


class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1


# print(Solution().firstMissingPositive([1, 2, 0]))
# print(Solution().firstMissingPositive([3, 4, -1, 1]))
# print(Solution().firstMissingPositive([7, 8, 9, 11, 12]))
print(Solution().firstMissingPositive([1, 1]))  # !重复标记

