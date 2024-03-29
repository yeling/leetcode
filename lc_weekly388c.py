
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
    # 247 / 631 个通过测试用例
    def shortestSubstrings(self, arr: List[str]) -> List[str]:   
        cache = defaultdict(set)
        for k,v in enumerate(arr):
            sn = len(v)
            for i in range(sn):
                for j in range(i+1,sn + 1):
                    cache[v[i:j]].add(k)
        ans = []
        for k,v in enumerate(arr):
            sn = len(v)
            temp = []
            for i in range(sn):
                for j in range(i+1,sn + 1):
                    if len(cache[v[i:j]]) == 1:
                        temp.append(v[i:j])
            if len(temp) > 0:
                # print(temp)
                temp.sort(key=lambda x: len(x))
                # print(temp)
                td = []
                for t in temp:
                    if len(t) == len(temp[0]):
                        td.append(t)
                    else:
                        break
                td.sort()
                ans.append(td[0])
            else:
                ans.append("")

        # print(cache)
        return ans
    
arr = ["cab","ad","bad","c"]
arr = ["abc","bcd","abcd"]
arr = ["gfnt","xn","mdz","yfmr","fi","wwncn","hkdy"]
sol = Solution()
print(sol.shortestSubstrings(arr))
