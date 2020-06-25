# dp[i] 表示字符串 ss 前 ii 个字符组成的字符串 s[0..i-1]s[0..i−1] 是否能被空格拆分成若干个字典中出现的单词
# dp[i]=dp[j] && check(s[j..i−1])

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True, s[0] in wordDict]
        for i in range(1, len(s)):
            for j in range(i+1):
                if s[j: i+1] in wordDict and dp[j]:
                    dp.append(True)
                    break
            else:
                dp.append(False)
        return dp[-1]

# 作者：ting-ting-28
# 链接：https://leetcode-cn.com/problems/word-break/solution/python3-dong-tai-gui-hua-by-ting-ting-28-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。