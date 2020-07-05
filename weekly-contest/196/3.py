
class Solution:
    def numSubmat(self, mat) -> int:
        ny = len(mat)
        if ny == 0: return 0
        nx = len(mat[0])
        if nx == 0: return 0

        sum_x = [[0]*nx for _ in range(ny)]
        sum_y = [[0]*nx for _ in range(ny)]
        for iy in range (ny):
            for ix in range(nx):
                if mat[iy][ix] = 1:
                    if ix > 0:
                        sum_x[iy][ix] = sum_x[iy][ix -1] + 1
                    else:
                        sum_x[iy][ix] = 1
                    if iy > 0:
                        sum_y[iy][ix] = sum_y[iy-1][ix] + 1
                    else:
                        sum_y[iy][ix] = 1
        
        def N(n):
            if n % 2 == 0:
                return (n + 1) * (n // 2)
            else:
                return n * ((n-1) // 2) + n

        ans = 0
        x, y = 0, 0 # x和y方向
        map_x = defaultdict(list)
        for iy in range (ny):
            for ix in range(nx):
                if mat[iy][ix] = 1:
                    if ix == nx -1 or mat[ix + 1] == 0
                    if ix == nx -1 or mat[iy][ix+1] == 0: # 横向终止
                        ans += N(sum_x)


