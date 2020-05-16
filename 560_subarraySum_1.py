#https://leetcode-cn.com/problems/subarray-sum-equals-k/

# sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.
# k = pre[j] - pre[i] -> pre[i] = pre[j] - k -> count(pre[j] - k)?

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return 0

        res = 0
        D = {}
        D[0] = 1 # itself
        Sum = 0
        for i in range(len(nums)):
            Sum += nums[i]
            Need = Sum - k
            if Need in D:
                res += D[Need]
            if Sum in D:
                D[Sum] += 1
            else:
                D[Sum] = 1
                
        return res

print (Solution().subarraySum([1,1,1], 2))