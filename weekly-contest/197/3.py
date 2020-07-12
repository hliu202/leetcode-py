from util.common_imports import *


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start: int,
        end: int,
    ) -> float:
        graph = defaultdict(dict)
        costs = defaultdict(float)
        for i in range(len(edges)):
            graph[edges[i][0]][edges[i][1]] = succProb[i]
            graph[edges[i][1]][edges[i][0]] = succProb[i]

        processed = set()
        worklist = set()
        n = start
        costs[start] = 1

        def find_high():
            high = 0
            tn = None
            for node in worklist:
                if node in processed:
                    continue

                c = costs[node]
                if c > high:
                    tn = node
                    high = c

            if tn:
                worklist.remove(tn)
            return tn

        while n is not None:
            cost = costs[n]
            # del costs[n]
            neighbors = graph[n]
            for neig in neighbors.keys():
                new_cost = cost * neighbors[neig]
                if neig in costs:
                    if costs[neig] < new_cost:
                        costs[neig] = new_cost
                        worklist.add(neig)
                else:
                    worklist.add(neig)
                    costs[neig] = new_cost
            processed.add(n)
            if n == end:
                return costs[n]
            n = find_high()

        return 0


print(
    Solution().maxProbability(
        n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.2], start=0, end=2
    )
)
print(
    Solution().maxProbability(
        n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.3], start=0, end=2
    )
)
print(Solution().maxProbability(n=3, edges=[[0, 1]], succProb=[0.5], start=0, end=2))
print(
    Solution().maxProbability(
        n=5,
        edges=[[1, 4], [2, 4], [0, 4], [0, 3], [0, 2], [2, 3]],
        succProb=[0.37, 0.17, 0.93, 0.23, 0.39, 0.04],
        start=3,
        end=4,
    )
)  # 0.2139

# !如果没有加worklist，会超出时间限制
