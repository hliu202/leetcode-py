# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def list_len(nums):
            if nums is None:
                return 0
            else:
                return len(nums)

        L1 = list_len(nums1)
        L2 = list_len(nums2)
        LEN = L1 + L2

        even = False
        # limit 即 median 的顺序 idx
        if LEN & 1 == 0:
            even = True
            limit = ((L1 + L2) >> 1) - 1
        else:
            limit = (L1 + L2) >> 1

        def get_median_from_1(nums, idx):
            if even:
                return (nums[idx] + nums[idx+1]) / 2
            else:
                return nums[idx]

        if L1 == 0:
            return get_median_from_1(nums2, limit)
        if L2 == 0:
            return get_median_from_1(nums1, limit)

        i, j = 0, 0
        while i < L1 and j < L2:
            if i + j == limit:
                break

            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        if i == L1: #
            return get_median_from_1(nums2, limit - i)
        if j == L2:
            return get_median_from_1(nums1, limit - j)

        if not even:
            return min(nums1[i], nums2[j])
        
        if nums1[i] < nums2[j]:
            N1 = nums1[i]
            if i + 1 < L1:
                N2= min(nums1[i+1], nums2[j])
            else:
                N2= nums2[j]
        else:
            N1 = nums2[j]
            if j+1 < L2:
                N2 = min(nums1[i], nums2[j+1])
            else:
                N2 = nums1[i]
        return (N1+N2) / 2

# print(Solution().findMedianSortedArrays([1,3], [2]))
# print(Solution().findMedianSortedArrays([1,2], [3,4]))
# print(Solution().findMedianSortedArrays([0,0], [0,0]))
# print(Solution().findMedianSortedArrays([1,2], [-1,3]))
# print(Solution().findMedianSortedArrays([1,2], [1,1]))
print(Solution().findMedianSortedArrays([1], [2,3]))
