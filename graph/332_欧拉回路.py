class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(curr: str):
            while vec[curr]:
                tmp = heapq.heappop(vec[curr])
                dfs(tmp)
            stack.append(curr)

        vec = collections.defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)
        for key in vec:
            heapq.heapify(vec[key])
        
        stack = list()
        dfs("JFK")
        return stack[::-1]
        
# !最小堆
# !当我们遍历完一个节点所连的所有节点后，我们才将该节点入栈（即逆序入栈）。

# Hierholzer 算法用于在连通图中寻找欧拉路径，其流程如下：
# 0. 从起点出发，进行深度优先搜索。
# 1. 每次沿着某条边从某个顶点移动到另外一个顶点的时候，都需要删除这条边。
# 2. 如果没有可移动的路径，则将所在节点加入到栈中，并返回。

# https://leetcode-cn.com/problems/reconstruct-itinerary/solution/zhong-xin-an-pai-xing-cheng-by-leetcode-solution/
