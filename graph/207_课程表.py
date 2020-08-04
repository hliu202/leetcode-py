from util.common_imports import *

# 图的拓扑排序
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graphs = defaultdict(list)
        for edge in prerequisites:
            graphs[edge[1]].append(edge[0])

        NOT_VISIT, VISITING, DONE = 0, 1, 2
        status = [NOT_VISIT] * numCourses
        valid = True

        def dfs(cur):
            nonlocal valid
            status[cur] = VISITING  # 更新状态为 VISITING

            for next in graphs[cur]:
                if status[next] == NOT_VISIT:  # 未搜索
                    dfs(next)
                    if not valid:
                        return
                elif status[next] == VISITING:  # 发现环
                    valid = False
                    return

            status[cur] = DONE

        for i in range(numCourses):
            if i in graphs:
                dfs(i)
                if not valid:
                    return False
        return True


print(Solution().canFinish(2, [[1, 0], [0, 1]]))
print(Solution().canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
