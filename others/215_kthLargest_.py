class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 替换nums[i]后维护最小堆：自顶向下调整新元素位置，直至该值满足(parent value < son value)
        def shift(i, k):
            flag = 0
            while (i * 2 + 1) < k and flag == 0:
                t = i
                if nums[i] > nums[2 * i + 1]:
                    t = 2 * i + 1
                if (i * 2 + 2) < k and nums[t] > nums[2 * i + 2]:
                    t = 2 * i + 2
                if t == i:
                    flag = 1
                else:
                    nums[i], nums[t] = nums[t], nums[i]
                    i = t

        # O(k):建立大小为K的最小堆， k/2-1是最后一个非叶节点，因为shift是向下调整，所以倒序从最下面出发，不然(4 32 1)->(2 34 1)->(2 14 3)->(2 14 3) 结果不对
        for i in range(k // 2, -1, -1):
            shift(i, k)

        # O((N-k)logK)，剩余元素依次比较替换
        for i in range(k, len(nums)):
            if nums[0] < nums[i]:
                nums[0] = nums[i]
                shift(0, k)
        return nums[0]
        # sum=O(Nlogk-k(logK-1))


# 作者：garfield-12
# 链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/quan-shou-xie-20xing-kge-yuan-su-de-zui-xiao-dui-d/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
