class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        L = sentence.split(' ')
        for i,v in enumerate(L):
            if v.startswith(searchWord):
                return i + 1
        return -1

print (Solution().isPrefixOfWord(sentence = "i love eating burger", searchWord = "burg"))
print (Solution().isPrefixOfWord(sentence = "this problem is an easy problem", searchWord = "pro"))
print (Solution().isPrefixOfWord(sentence = "i am tired", searchWord = "you"))
print (Solution().isPrefixOfWord(sentence = "i use triple pillow", searchWord = "pill"))
print (Solution().isPrefixOfWord(sentence = "hello from the other side", searchWord = "they"))

