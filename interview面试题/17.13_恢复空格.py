# https://leetcode-cn.com/problems/re-space-lcci/


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        """
        动态规划
        状态定义：f[i]，0 <= i <= len(sentence)
            集合：前 i 个字符所有可能的划分方式
            属性：Min(未识别的字符数)
        状态转移：
            集合划分：
                第 i 个字符无法与前面任何一个子串组成单词：f[i - 1] + 1
                第 i 个字符可以与前面某个子串组成单词：f[j]
                if sentence[j:i] in dictionary，0 <= j <= i - 1
            初始化：f[0] = 0，当 sentence 为空字符串时，未识别字符数为 0
            答案：f[-1]
        """
        d = {}.fromkeys(dictionary)
        n = len(sentence)
        f = [0] * (n + 1)
        for i in range(1, n + 1):
            f[i] = f[i - 1] + 1
            for j in range(i):
                if sentence[j:i] in d:
                    f[i] = min(f[i], f[j])
        return f[-1]


# 作者：acw_jpch89
# 链接：https://leetcode-cn.com/problems/re-space-lcci/solution/python-3dong-tai-gui-hua-by-acw_jpch89-4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
