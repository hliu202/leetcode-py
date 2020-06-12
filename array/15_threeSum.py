class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        res = []
        for i in range(0, n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue # 避免重复结果

            T = - nums[i]
            j, k = i+1, n - 1
            while j < k:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1 # 避免重复结果
                    continue

                if nums[j] + nums[k] < T:
                    j += 1
                elif nums[j] + nums[k] > T:
                    k -= 1
                else:
                    r = [nums[i], nums[j], nums[k]]
                    res.append(r)
                    j += 1 # 不能 break，还有其他结果
                    k -= 1
        return res


# print(Solution().threeSum([0, 0, 0, 0]))
print(Solution().threeSum([-1,0,1,2,-1,-4]))  # [[-1,-1,2],[-1,0,1]]
