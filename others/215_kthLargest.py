from util.common_imports import *


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        i, n = 0, len(nums)
        left, mid, right = [], [], []
        m = nums[0]
        mid.append(m)
        for j in range(1, n):
            if nums[j] < m:
                left.append(nums[j])
            elif nums[j] > m:
                right.append(nums[j])
            else:
                mid.append(nums[j])

        n_right = len(right)
        n_mid = len(mid)
        if n_right < k:
            if n_right + n_mid >= k:
                return m
            else:  # k > n_right+n_mid
                return self.findKthLargest(left, k - (n_right + n_mid))
        else:  # k <= n_right
            return self.findKthLargest(right, k)


print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))

