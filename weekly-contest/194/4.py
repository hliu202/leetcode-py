# https://leetcode-cn.com/contest/weekly-contest-194/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        _edges = edges
        edges = [e + [i] for i, e in enumerate(edges)]
        edges.sort(key=lambda x: x[2])
        def find_anc(anc, i):
            if anc[i] == i:
                return i
            j = find_anc(anc, anc[i])
            anc[i] = j
            return j
        
        def mst(rm, inc):
            anc = list(range(n))
            cost, cnt = 0, 0
            
            if inc != -1:
                u, v, c = _edges[inc]
                cost = c
                cnt = 1
                anc[u] = v
                
            for u, v, c, i in edges:
                if i == rm or i == inc:
                    continue
                if find_anc(anc, u) != find_anc(anc, v):
                    anc[anc[u]] = anc[v]
                    cost += c
                    cnt += 1
            return cost, cnt
                
        best_cost, _ = mst(-1, -1)
        crit, non_crit = [], []
        
        for i in range(len(edges)):
            cost, cnt = mst(i, -1)
            if cnt < n - 1 or cost > best_cost:
                crit.append(i)
            else:
                cost, cnt = mst(-1, i)
                if cost == best_cost and cnt == n - 1:
                    non_crit.append(i)
                
        return crit, non_crit