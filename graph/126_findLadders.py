from util.common_imports import *

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)
        ### 构建具有邻接关系的桶
        buckets = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                match = word[:i] + '_' + word[i+1:]
                buckets[match].append(word)
        ##### BFS遍历
        preWords = defaultdict(list)#前溯词列表
        toSeen = deque([(beginWord, 1)])#待遍历词及深度列表
        beFound = {beginWord:1}#已探测词词列表
        while toSeen:
            curWord, level = toSeen.popleft()
            for i in range(len(beginWord)):
                match = curWord[:i] + '_' + curWord[i+1:]
                for word in buckets[match]:
                    if word not in beFound:
                        beFound[word] = level+1
                        toSeen.append((word, level+1))
                    if beFound[word] == level+1:#当前深度等于该词首次遍历深度，则仍应加入前溯词列表
                        preWords[word].append(curWord)
            if endWord in beFound and level+1 > beFound[endWord]:#已搜索到目标词，且完成当前层遍历
                break
        #### 列表推导式输出结果
        if endWord in beFound:
            res = [[endWord]]
            while res[0][0] != beginWord:
                res = [[word] + r for r in res for word in preWords[r[0]]] 
            return res
        else:
            return []

# beFound：用于标记首次遍历的词，同时记录首次遍历的深度
# preWords：用一个默认列表字典记录到达该节点的前溯词列表，这里需注意对于每个可能搜索到该词的路径，只要深度不超过已有路径，都应加入前溯词列表
# toSeen：用一个双端队列存储待遍历词及当前深度。

# 作者：luanhz
# 链接：https://leetcode-cn.com/problems/word-ladder-ii/solution/pythontong-yan-du-you-xian-sou-suo-by-luanz/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

print (Solution().findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"])) 
# print (Solution().findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))
