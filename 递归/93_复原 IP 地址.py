from util.common_imports import *


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        segments = [""] * 4 # 0-255,...
        n = len(s)

        def dfs(start, id):
            if id == 4:
                if start == n:
                    ans.append('.'.join(segments))
                return
            if start == n:
                return
            
            #! "0"特殊情况
            if s[start] == "0":
                segments[id] = "0"
                dfs(start+1, id+1)
                return
                
            for i in range(4):
                if start + i < n:
                    cur = int(s[start:i+start + 1])
                    if cur < 256:
                        segments[id] = s[start:i+start + 1]
                        dfs(start+i + 1, id + 1)

        dfs(0,0)
        return ans

print(Solution().restoreIpAddresses("25525511135"))
print(Solution().restoreIpAddresses("0000"))
