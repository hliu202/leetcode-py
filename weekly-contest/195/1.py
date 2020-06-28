from util.common_imports import *
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        self.D = defaultdict(set)
        self.D[0].add(0)
        x, y = 0, 0

        for v in path:
            if v == 'N':
                y += 1
            elif v == 'E':
                x += 1
            elif v == 'S':
                y -=1
            else: # 'W'
                x -= 1

            if y in self.D[x]:
                return True
            else:
                self.D[x].add(y)
        return False
print (Solution().isPathCrossing(path = "NESWW"))
print (Solution().isPathCrossing(path = "NESSSEEN"))