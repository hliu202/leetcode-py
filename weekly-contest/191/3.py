from util.common_imports import *
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        D = defaultdict(set)
        Arr = set()
        res = 0
        for v in connections:
            if v[0] == 0: Arr.add(v[1])
            elif v[1] == 0: 
                Arr.add(v[0])
                res += 1
            else:
                D[v[0]].add(v[1])
        
        def find_next():
            nonlocal res
            for k in D.keys():
                if k in Arr:
                    return k
                else:
                    for v in D[k]:
                        if v in Arr:
                            res += 1
                            return k

        while D:
            k = find_next()
            Arr.add(k)
            Arr.update(D[k])
            del D[k]

        return n-1 - res


print(Solution().minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]))
print(Solution().minReorder(n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]))
print(Solution().minReorder(n = 3, connections = [[1,0],[2,0]]))
print(Solution().minReorder(10, [[0,1],[2,1],[3,2],[0,4],[5,1],[2,6],[5,7],[3,8],[8,9]]))