
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
from heapq import *
import string
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

def prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

class Solution:
    # OOM 593 / 596 个通过测试用例
    # TLE 594 / 596 个通过测试用例
    def countPrefixSuffixPairs2(self, words: List[str]) -> int: 
        ans = 0
        cache = defaultdict(int)
        n = len(words)
        for i in range(n):
            for j in range(len(words[i])):
                t = words[i][0:j+1]
                if t == words[i][-(j + 1):] and cache[t] > 0:
                    ans += cache[t]
            cache[words[i]] += 1
        
        return ans
    
    
    def countPrefixSuffixPairs(self, words: List[str]) -> int: 
        ans = 0
        cache = defaultdict(int)
        n = len(words)
        for i in range(n):
            pn = prefix_function(words[i])
            
            for v in pn:
                t = words[i][0:v]
                if t in cache:
                    ans += cache[t]
            ans += cache[words[i]] 
            cache[words[i]] += 1
            print(pn, ans, i)
        
        return ans
    
words = ["a","aba","ababa","aa"]
words = ["a", "a"]
# words = ["ab", "abc"]
# words = ["pa","papa","ma","mama"]
# words = ["cbbca","ac","ac"]
words = ["aaa","baa","b","bcba"]

sol = Solution()
print(sol.countPrefixSuffixPairs(words))
print(sol.countPrefixSuffixPairs2(words))

