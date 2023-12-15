
# auther yeling
from typing import List
from bisect import *
from collections import *

MOD = 10 ** 9 + 7

class Solution:
    # 23 / 34
    # 33 / 34
    # AC
    def expressiveWords(self, s: str, words: List[str]) -> int:
        res = 0
        for w in words:
            if len(w) + 2 > len(s):
                continue
            i,j = 0,0
            while i < len(w):
                count = 0
                dst = w[i]
                wcount = 1
                while i < len(w) - 1 and w[i] == w[i+1]:
                    i += 1
                    wcount += 1
                    
                while j < len(s) and s[j] == dst:
                    count += 1
                    j += 1
                if count < wcount or wcount == 1 and count == 2:
                    break
                i += 1

            if j == len(s) and i == len(w):
                # print(w)
                res += 1

        return res

s = "heeelllooo"
words = ["hello", "hi", "helo"]
s = "ddiiiinnssssssoooo"
words = ["dinso","ddiinnso","ddiinnssoo","ddiinso"]

sol = Solution()
print(sol.expressiveWords(s,words))
