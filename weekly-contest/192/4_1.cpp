const int INF = 1000000000;
int f[111][22][111];

class Solution {
public:
    int minCost(vector<int>& houses, vector<vector<int>>& cost, int m, int n, int target) {
        for (int i = 0; i <= m; ++ i)
            for (int j = 0; j <= n; ++ j)
                for (int k = 0; k <= target; ++ k)
                    f[i][j][k] = INF;
        f[0][0][0] = 0;
        for (int i = 0; i < m; ++ i)
            for (int j = 0; j <= n; ++ j)
                for (int k = 0; k <= target; ++ k)
                {
                    if (f[i][j][k] == INF) continue;
                    if (houses[i] != 0)
                    {
                        int x = houses[i];
                        f[i+1][x][k+(j!=x)] = min(f[i+1][x][k+(j!=x)], f[i][j][k]);
                    }
                    else
                    {
                        for (int x = 1; x <= n; ++ x)
                        {
                            f[i+1][x][k+(j!=x)] = min(f[i+1][x][k+(j!=x)], f[i][j][k]+cost[i][x-1]);
                        }
                    }
                }
        int ret = INF;
        for (int j = 1; j <= n; ++ j)
            ret = min(ret, f[m][j][target]);
        if (ret == INF) ret = -1;
        return ret;
    }
};