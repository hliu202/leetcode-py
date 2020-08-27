from util.common_imports import *
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets: return []

        G = defaultdict(list)
        for t in tickets:
            G[t[0]].append(t[1])
        
        for ts in G.values():
            ts.sort()

        def tr(cur):
            nonlocal ans
            if not G[cur]:
                return

            next = G[cur][0]
            is1stTerm = False
            if len(G[cur]) > 1:  # 避免 next 是终点
                if next not in G or not G[next]:
                    is1stTerm = True
                    next = G[cur][1]
                    del G[cur][1]
            
            if not is1stTerm:
                del G[cur][0]

            ans.append(next)
            tr(next)
        
        ans = ["JFK"]
        tr("JFK")
        return ans

# print(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
# print(Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(Solution().findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])) # ["JFK","NRT","JFK","KUL"]
print(Solution().findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]))
# expect: ["JFK","AXA","AUA","ADL","ANU","AUA","ANU","EZE","ADL","EZE","ANU","JFK","AXA","EZE","TIA","AUA","AXA","TIA","ADL","EZE","HBA"]
# myans:  ["JFK","AXA","AUA","ADL","ANU","AUA","ANU","EZE","ADL","EZE","ANU","JFK","AXA","EZE","TIA",                  "ADL","EZE","HBA"] # 有的结果被忽略了...