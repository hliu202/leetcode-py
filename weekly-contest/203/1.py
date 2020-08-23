from util.common_imports import *

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        s, e = rounds[0], rounds[-1]
        if s <= e:
            ans = list(range(s, e+1))
        else:
            ans = list(range(1, e+1))
            ex = list(range(s, n+1))
            ans.extend(ex)

        return ans


# print(Solution().mostVisited(n = 4, rounds = [1,3,1,2]))
# print(Solution().mostVisited(n = 2, rounds = [2,1,2,1,2,1,2,1,2]))
# print(Solution().mostVisited(n = 7, rounds = [1,3,5,7]))
print(Solution().mostVisited(n = 7, rounds = [5,2]))
