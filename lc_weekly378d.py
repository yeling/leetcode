
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
    # 71 / 1209 个
    # 87 / 1209 个通过测试用例
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        s1 = s[0:n//2]
        s2 = s[n-1:n//2 - 1:-1]
        print(s1, s2)
        ps1 = [[0] * 26 for _ in range(n//2 + 1)]
        ps2 = [[0] * 26 for _ in range(n//2 + 1)]
        diff = []
        pos = -1
        for i in range(n//2):
            ps1[i + 1] = ps1[i][:]
            ps1[i + 1][ord(s1[i]) - ord('a')] += 1

            ps2[i + 1] = ps2[i][:]
            ps2[i + 1][ord(s2[i]) - ord('a')] += 1

            if s1[i] != s2[i]:
                if pos == -1:
                    pos = i
            else:
                if pos != -1:
                    diff.append((pos,i-1))
                pos = -1
        if pos != -1:
            diff.append((pos,n//2 - 1))
        print(diff)
        def check(s,e):
            # print("check", s, e)
            for i in range(26):
                if ps1[e + 1][i] - ps1[s][i] == ps2[e + 1][i] - ps2[s][i]:
                    continue
                else:
                    return False
            
            return True
        
        ans = []

        for a,b,c,d in queries:
            a2 = n - 1 - d
            b2 = n - 1 - c
            #两个区域
            if b < a2 or b2 < a:
                ret = check(a,b) and check(a2, b2)
                if ret == True:
                    if len(diff) > 0:
                        if diff[0][0] < min(a, a2) or diff[-1][1] > max(b, b2):
                            ret = False
                        else:
                            if b < a2:
                                p1 = bisect_left(diff, b, key=lambda x:x[0]) 
                                if diff[p1[0]] < a2:
                                    ret = False
                            elif b2 < a:
                                p1 = bisect_left(diff, b2, key=lambda x:x[0]) 
                                if diff[p1[0]] < a:
                                    ret = False
                ans.append(ret)    
            else:
                #这里有问题
                s = min(a, a2)
                e = max(b, b2)
                ret = check(s,e)
                if len(diff) > 0:
                    if diff[0][0] >= s and diff[-1][1] <= e:
                        ret = ret and True
                    else:
                        ret = False
                ans.append(ret)

        return ans
    
s = "abcabc"
queries = [[1,1,3,5],[0,2,5,5]]
s = "abbcdecbba"
queries = [[0,2,7,9]]
s = "acbcab"
queries = [[1,2,4,5]]

s = "odaxusaweuasuoeudxwa"
queries = [[0,5,10,14]]

sol = Solution()
print(sol.canMakePalindromeQueries(s, queries))
