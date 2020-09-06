class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        cur = []

        def checkvalid(x, y):
            
        for i in range(0, n): # 第几行
            for j in range(0, n): # 第几列
                if i = 0:
                    line = ''.join(['.']*n)
                    line[j] = 'Q'
                    cur.append(line)
                else:
                    checkvalid(i, j)
