from util.common_imports import *

# dfs
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * n
        valid = True

        def dfs(node: int, c: int):
            nonlocal valid
            color[node] = c
            cNei = (GREEN if c == RED else RED)
            for neighbor in graph[node]:
                if color[neighbor] == UNCOLORED:
                    dfs(neighbor, cNei)
                    if not valid:
                        return
                elif color[neighbor] != cNei:
                    valid = False
                    return

        for i in range(n):
            if color[i] == UNCOLORED:
                dfs(i, RED)
                if not valid:
                    break
        
        return valid



# print(Solution().isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
# print(Solution().isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
print(Solution().isBipartite([[1], [0, 3], [3], [1, 2]]))

