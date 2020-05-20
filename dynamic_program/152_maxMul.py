# https://leetcode-cn.com/problems/maximum-product-subarray/
from typing import List

# pos : 包含 i-1 的，最大正 乘积, 负数表示没有
# neg : 包含 i-1 的，最小负 乘积, 正数表示没有

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pos = -1
        neg = 1
        res = nums[0]
        
        for cur in nums:
            if cur == 0:
                pos = -1
                neg = 1
                res = max(res, 0)
            elif cur < 0: # stop pos
                tmp_pos = pos
                pos = neg*cur # if neg < 0, neg*cur is max pos, if neg >0, neg * cur < 0
                neg = min(cur, tmp_pos*cur) # if pos >0, pos*cur is min neg, if pos <0, choose cur
                res = max(res, pos)
            else: # cur > 0
                neg *= cur # if neg <0, neg*cur is min neg， if neg >0, neg * cur > 0
                pos = max(cur, pos*cur)
                res = max(pos, res)
        return res



print(Solution().maxProduct([2,3,-2,4]))
print(Solution().maxProduct([-2,0,-1]))
print(Solution().maxProduct([-1,-2,-9,-6]))
                

