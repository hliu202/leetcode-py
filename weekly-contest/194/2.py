from util.common_imports import *

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        N = defaultdict(int)
        res = []
        for v in names:
            if v not in N:
                N[v] = 0
                res.append(v)
            else:
                k = N[v]
                k += 1
                while True:
                    new_n = v + '(' + str(k) + ')'
                    if new_n in N:
                        k += 1
                    else:
                        break
                N[v] = k
                N[new_n] = 0
                res.append(new_n)
        return res

# print (Solution().getFolderNames(names = ["pes","fifa","gta","pes(2019)"]))
# print (Solution().getFolderNames(names = ["gta","gta(1)","gta","avalon"]))
# print (Solution().getFolderNames(names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]))
# print (Solution().getFolderNames(names = ["wano","wano","wano","wano"]))
# print (Solution().getFolderNames(names = ["kaido","kaido(1)","kaido","kaido(1)"]))
print (Solution().getFolderNames(["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]))