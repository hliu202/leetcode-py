
# 树状数组
class BinaryIndexedTree:
    def __init__(self, nums):

        self.BIT_arr = [0] * (len(nums) + 1)
        # O(nlogn)
        # for i in range(len(nums)):
        #     self.updata(i, nums[i])
        # O(n)
        for i in range(len(nums)):
            self.BIT_arr[i + 1] = nums[i]
        for i in range(1, len(self.BIT_arr)):
            j = i + (i & -i)
            if j < len(self.BIT_arr):
                self.BIT_arr[j] += self.BIT_arr[i]

    # 更新,是指在i位置上加上 val
    def updata(self, i, delta):
        i += 1
        while i < len(self.BIT_arr):
            self.BIT_arr[i] += delta
            i += i & (-i)

    # 重新赋值, 在i位置为val
    def setVal(self, i, val):
        i += 1
        self.updata(i, val - self.BIT_arr[i])

    def prefix(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.BIT_arr[i]
            i -= i & (-i)
        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}
        # print(hashTable)
        tree = BinaryIndexedTree([0] * len(hashTable))
        res = []
        for i in range(len(nums) - 1, -1, -1):
            res.append(tree.prefix(hashTable[nums[i]] - 1))
            tree.updata(hashTable[nums[i]], 1)

        return res[::-1]


# 线段树
class SegmentTree(object):
    def __init__(self, nums):
        self.l = len(nums)
        self.tree = [0] * self.l + nums
        for i in range(self.l - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    # 重新赋值, 在i位置为val
    def setVal(self, i, val):
        n = self.l + i
        self.tree[n] = val
        while n > 1:
            self.tree[n >> 1] = self.tree[n] + self.tree[n ^ 1]
            n >>= 1

    # 更新,是指在i位置上加上 val
    def updata(self, i, val):
        n = self.l + i
        tmp = self.tree[n]
        self.setVal(i, tmp + val)

    def sumRange(self, i: int, j: int) -> int:
        m = self.l + i
        n = self.l + j
        res = 0
        while m <= n:
            if m & 1:
                res += self.tree[m]
                m += 1
            m >>= 1
            if n & 1 == 0:
                res += self.tree[n]
                n -= 1
            n >>= 1
        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}
        tree, r = SegmentTree(len(hashTable) * [0]), []
        for i in range(len(nums) - 1, -1, -1):
            r.append(tree.sumRange(0, hashTable[nums[i]] - 1))
            tree.updata(hashTable[nums[i]], 1)
        return r[::-1]


# 二叉搜索树 + 维护左子树count：insert时累加count
