from util.common_imports import *


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i + 1]:
                return numbers[i + 1]
        return numbers[0]


print(Solution().minArray([3, 4, 5, 1, 2]))
print(Solution().minArray([1,3,5]))
