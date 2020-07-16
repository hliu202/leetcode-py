from util.common_imports import *


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()
        S0, S1 = set(), set()
        worklist = [0]

        while worklist or len(visited) < len(graph):
            if worklist:
                next = worklist.pop()
            else:
                for i in range(len(graph)):
                    if i not in visited:
                        next = i
                        break

            visited.add(next)

            if next in S0:
                in_s0 = True
            elif next in S1:
                in_s0 = False
            else:
                in_s0 = None
                for j in graph[next]:
                    if j in S0:
                        S1.add(next)
                        in_s0 = False
                        break
                    elif j in S1:
                        S0.add(next)
                        in_s0 = True
                        break
                if in_s0 is None:
                    S0.add(next)
                    in_s0 = True

            for j in graph[next]:
                if in_s0:
                    if j in S0:
                        return False
                    elif j not in visited:
                        S1.add(j)
                        worklist.append(j)
                else:
                    if j in S1:
                        return False
                    elif j not in visited:
                        S0.add(j)
                        worklist.append(j)

        return True


# print(Solution().isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
# print(Solution().isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
print(Solution().isBipartite([[1], [0, 3], [3], [1, 2]]))

