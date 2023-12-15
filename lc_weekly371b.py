
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

class Solution:
    # 1126 / 1143
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]: 
        cache = defaultdict(list)
        for i,t in access_times:
            cache[i].append(int(t))
        ans = []
        # print(cache)
        for k in cache:
            l = 0
            r = 0
            cache[k].sort()
            while r < len(cache[k]):
                flag = False
                if cache[k][r] - cache[k][l] < 100:
                    if r - l + 1 >= 3:
                        ans.append(k)
                        flag = True
                        break
                    if flag:
                        break  
                    r += 1       
                else:
                    l += 1
            
                
        return ans
    
access_times = [["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]]
access_times = [["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]]
access_times = [["qzgyyji","1945"],["qzgyyji","1855"],["jsxkxtugi","1859"],["hhjuaxal","1940"],["hhjuaxal","1831"],["jsxkxtugi","1841"],["hhjuaxal","1918"],["jsxkxtugi","1941"],["hhjuaxal","1852"]]
sol = Solution()
print(sol.findHighAccessEmployees(access_times))
