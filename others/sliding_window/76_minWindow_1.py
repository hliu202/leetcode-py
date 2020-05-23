class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        from collections import Counter
        t = Counter(t)  # !! counter and lambda
        lookup = Counter()
        start = 0
        end = 0
        min_len = float("inf")
        res = ""
        while end < len(s):
            lookup[s[end]] += 1
            end += 1
            #print(start, end)
            while all(map(lambda x: lookup[x] >= t[x], t.keys())):
                if end - start < min_len:
                    res = s[start:end]
                    min_len = end - start
                lookup[s[start]] -= 1
                start += 1
        return res

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/minimum-window-substring/solution/hua-dong-chuang-kou-by-powcai-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。