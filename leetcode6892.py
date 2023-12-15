
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

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                flag = True
                if len(words[i]) == len(words[j]):
                    for k in range(len(words[i])):
                        if words[i][k] == words[j][-1-k]:
                            continue
                        else:
                            flag = False
                            break
                else:
                    flag = False
                if flag:
                    ans += 1
                    break
            
        return ans
    
words = ["cd","ac","dc","ca","zz"]
words = ["aa","ba","cc"]
sol = Solution()
print(sol.maximumNumberOfStringPairs(words))
