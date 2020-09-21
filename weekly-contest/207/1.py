from util.common_imports import *

class Solution:
    def reorderSpaces(self, text: str) -> str:
        count_words, count_space = 0, 0
        i,n = 0, len(text)
        words = []
        while i < n:
            if text[i] == ' ':
                count_space += 1
                i += 1
            else:
                cur_word = ''
                while i < n and text[i] != ' ':
                    cur_word += text[i]
                    i += 1
                words.append(cur_word)
                count_words += 1

        if count_space == 0: return text
        if count_words == 1:
            ns = 0
        else:
            ns = count_space // (count_words - 1)

        spaces = ' '*ns
        ans = spaces.join(words) + ' ' * (count_space - ns*(count_words-1))
        return ans
        # print("'" + ans + "'")

print(Solution().reorderSpaces("  this   is  a sentence "))
print(Solution().reorderSpaces("  walks  udp package   into  bar a"))
print(Solution().reorderSpaces("    a"))