from util.common_imports import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        A = [list('abc'), list('def'), list('ghi'), list('jkl'), list('mno'), list('pqrs'), list('tuv'), list('wxyz')]

        def tra(idx):
            if idx == 0:
                return A[int(digits[0])-2]
            
            res = tra(idx - 1)
            cur_list = A[int(digits[idx])-2]

            res2 = []
            for L in res:
                for c in cur_list:
                    res2.append(L+c)
            return res2
    
        return tra(len(digits)-1)

print(Solution().letterCombinations('23'))
