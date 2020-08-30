from util.common_imports import *
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        cur_neg = 0
        cur_pos = 0
        for i in range(0,n):
            if nums[i] == 0:
                cur_neg, cur_pos = 0, 0
            elif nums[i] > 0:
                cur_pos += 1
                if cur_neg > 0:
                    cur_neg += 1
                ans = max(cur_pos, ans)
            else: # neg
                tmp_neg = cur_neg
                cur_neg = cur_pos + 1
                if tmp_neg > 0:
                    cur_pos = tmp_neg + 1
                    ans = max(cur_pos, ans)
                else:
                    cur_pos = 0 # 之前没有负数
        return ans

# print(Solution().getMaxLen(nums = [1,2,3,5,-6,4,0,10]))
print(Solution().getMaxLen(nums = [-1,-2,-3,0,1]))
print(Solution().getMaxLen(nums = [0,1,-2,-3,-4]))
print(Solution().getMaxLen([1,-2,-3,4]))
# print(Solution().getMaxLen(nums = [-1,2]))
