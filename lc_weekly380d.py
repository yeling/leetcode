
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
    def beautifulIndices2(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        an = len(a)
        bn = len(b)
        ap = []
        bp = []
        for i in range(n):
            ta = s[i:i+an]
            if ta == a:
                ap.append(i)
            tb = s[i:i+bn]
            if tb == b:
                bp.append(i)
        ans = []
        for v in ap:
            p1 = bisect_right(bp, v + k)
            p2 = bisect_left(bp, v - k)
            # print(v, p1, p2)
            if p1 - p2 > 0:
                ans.append(v)
        # print(ap, bp)
        return ans
    
    def strStr(self, haystack: str, needle: str) -> List[int]:
        def KMP(s, p):
            """
            s为主串
            p为模式串
            如果t里有p，返回打头下标
            """
            nex = getNext(p)
            i = 0
            j = 0   # 分别是s和p的指针
            ret = []
            
            for i in range(0, len(s)):
                # print("1", nex, j)
                while j > 0 and (j == len(p) or s[i] != p[j]):
                    j = nex[j]
                    # print("2", nex, j)

                if s[i] == p[j]:
                    j += 1
                if j == len(p):
                    ret.append(i - len(p) + 1)
               
            return ret

        def getNext(p):
            """
            p为模式串
            返回next数组，即部分匹配表
            """
            nex = [0] * (len(p) + 1)
            nex[0] = -1
            i = 0
            j = -1
            while i < len(p):
                if j == -1 or p[i] == p[j]:
                    i += 1
                    j += 1
                    nex[i] = j     # 这是最大的不同：记录next[i]
                else:
                    j = nex[j]

            return nex
        
        return KMP(haystack, needle)

    # 195 / 232 个通过测试用例
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        an = len(a)
        bn = len(b)
        ap = []
        bp = []
        ap = self.strStr(s,a)
        bp = self.strStr(s,b)
        # print(ap, bp)

        ans = []
        for v in ap:
            p1 = bisect_right(bp, v + k)
            p2 = bisect_left(bp, v - k)
            # print(v, p1, p2)
            if p1 - p2 > 0:
                ans.append(v)
        # print(ap, bp)
        return ans
    
s = "isawsquirrelnearmysquirrelhouseohmy"
a = "my"
b = "squirrel"
k = 15
s = "abcd"
a = "a"
b = "a"
k = 4
sol = Solution()
print(sol.beautifulIndices(s, a, b, k))

print(sol.beautifulIndices2(s, a, b, k))
