
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

def isPre(a,b):
    i = 0
    j = 0
    cnt = 0
    if len(b) - len(a) != 1:
        return False

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            j += 1
            i += 1
        else:
            cnt += 1
            j += 1
        if cnt > 1:
            return False
            
    return True

class Solution:
    # 73 / 84 
    # 75 / 84     
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key= lambda a:len(a))
        n = len(words)
        dp = [1]*n
        ans = 1
        for i in range(n):
            k = i + 1
            temp = words[i]
            while k < n and len(words[k]) - len(temp) <= 1:
                if isPre(temp, words[k]):
                    dp[k] = max(dp[k], dp[i] + 1)
                    ans = max(ans, dp[k])
                k += 1
        return ans

# print(isPre("xd","xdcc"))
words = ["xbc","pcxbcf","xc","cxbc","pcxbc"]
words = ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]
# words =["a","ab","ac","bd","abc","abd","abdd"]
sol = Solution()
print(sol.longestStrChain(words))
