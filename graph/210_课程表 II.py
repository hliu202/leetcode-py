# https://leetcode-cn.com/problems/course-schedule-ii/

# 图的拓扑排序
import collections


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        edges = collections.defaultdict(list)
        visited = [0] * numCourses  # 0: not, 1: visiting, 2: done
        stack = []
        valid = True

        for I in prerequisites:
            edges[I[-1]].append(I[0])

        def dfs(node):
            nonlocal valid
            visited[node] = 1

            for t in edges[node]:
                if visited[t] == 0:
                    dfs(t)
                elif visited[t] == 1:
                    valid = False
                    return

                if not valid:
                    return

            visited[node] = 2
            stack.append(node)

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
                if not valid:
                    return []  # None or Empty?

        return stack[::-1]


# print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(Solution().findOrder(2, [[0, 1], [1, 0]]))

