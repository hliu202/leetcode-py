# https://leetcode-cn.com/problems/sliding-window-maximum/
# 双端队列 滑动窗口最大值
#  - 只保留当前滑动窗口中有的元素的索引。
#  - 移除比当前元素小的所有元素，它们不可能是最大的。
import collections

nums = [1,3,-1,-3,5,3,6,7]
k = 3

# https://leetcode-cn.com/problems/sliding-window-maximum/solution/python-deque-by-dangerusswilson/
q, res = collections.deque(), []  
res.append(max(nums[:k]))
for i in range(len(nums)):
    while q and nums[i] > q[-1]:    # 移除队列尾部比 nums[i] 小的
        q.pop()
    q.append(nums[i])               # 加入队列
    if i-k >= 0:
        if nums[i-k] == q[0]:
            q.popleft()             # 移除上个窗口的
        res.append(q[0])            # 队列头始终是最大的
print (res)
