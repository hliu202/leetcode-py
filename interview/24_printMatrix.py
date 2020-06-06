# https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/

class Solution:
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res

print (Solution().spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

# zip 作用？
# unzip matrix，结合 list()，实现行列变换

