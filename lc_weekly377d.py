
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
    # 361 / 647 
    # 368 / 647 
    def minimumCost2(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:    
        cn = len(cost)
        grid = defaultdict(int)
        orgSet = set(original)
        chgSet = set(changed)
        for i in range(cn):
            for j in range(cn):
                grid[(original[i], changed[j])] = INF
                grid[(changed[j], original[i])] = INF

        for i in range(cn):
            if (original[i], changed[i]) in grid:
                grid[(original[i], changed[i])] = min(grid[(original[i], changed[i])],cost[i])
            else:
                grid[(original[i], changed[i])] = cost[i]
        # print(grid)
        # Floyd
        for k in range(cn):
            for i in range(cn):
                for j in range(cn):
                    grid[(original[i], changed[j])] = min(grid[(original[i], changed[j])], grid[(original[i], changed[k])] + grid[(changed[k], changed[j])])
        # print(grid)
        n = len(source)
        dp = [INF] * (n + 1)
        dp[0] = 0
        path = [[] for _ in range(n + 1)] 
        for i in range(n):
            for j in range(i, n):
                s = source[i:j + 1]
                t = target[i:j + 1]
                if s == t:
                    dp[j + 1] = min(dp[j + 1], dp[i])
                elif s in orgSet and t in chgSet :
                    dp[j + 1] = min(dp[j + 1], dp[i] + grid[(s,t)])
                print(dp[n])
        if dp[n] == INF:
            return -1       
        return dp[n]
    
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:    
        cn = len(cost)
        grid = defaultdict(int)
        orgSet = set(original)
        chgSet = set(changed)
        for i in range(cn):
            for j in range(cn):
                grid[(original[i], changed[j])] = INF
                grid[(changed[j], original[i])] = INF

        for i in range(cn):
            if (original[i], changed[i]) in grid:
                grid[(original[i], changed[i])] = min(grid[(original[i], changed[i])],cost[i])
            else:
                grid[(original[i], changed[i])] = cost[i]
        # print(grid)
        # Floyd
        for k in range(cn):
            for i in range(cn):
                for j in range(cn):
                    grid[(original[i], changed[j])] = min(grid[(original[i], changed[j])], grid[(original[i], changed[k])] + grid[(changed[k], changed[j])])
        # print(grid)
        n = len(source)
        dp = [INF] * (n + 1)
        dp[0] = 0
        path = [[] for _ in range(n + 1)] 
        for i in range(n):
            for j in range(i, n):
                s = source[i:j + 1]
                t = target[i:j + 1]
                if s == t:
                    if dp[j + 1] > dp[i]:
                        dp[j + 1] = dp[i]
                        tp = path[i][:]
                        tp.append(j)
                        path[j + 1] = tp
                    
                elif s in orgSet and t in chgSet :
                    if dp[j + 1] > dp[i] + grid[(s,t)]:
                        tp = path[i][:]
                        tp.append(j)
                        path[j + 1] = tp
                        dp[j + 1] = dp[i] + grid[(s,t)]
            
        print(dp[n], path[n])
        print(dp[n], path[4])
        sum = 0
        for i in range(1,len(path[n])):
            s = source[path[n][i-1]:path[n][i] + 1]
            t = target[path[n][i-1]:path[n][i] + 1]
            while (s not in orgSet or t not in chgSet) and len(s) > 0 and s[0] == t[0]:
                s = s[1:]
                t = t[1:]
            
            while (s not in orgSet or t not in chgSet) and len(s) > 0 and s[-1] == t[-1]:
                s = s[0:len(s) - 1]
                t = t[0:len(t) - 1]
            if s != t:
                sum += grid[(s,t)]
            print(s,t,sum)
        for v in chgSet:
            for k in orgSet:
                if v != "cb":
                    continue
                if len(v) == 2 and len(k) == 2:
                    print((k, v), grid[(k, v)])
        
            
        if dp[n] == INF:
            return -1       
        return dp[n]
    
source = "abcd"
target = "acbe"
original = ["a","b","c","c","e","d"]
changed = ["b","c","b","e","b","e"]
cost = [2,5,5,1,2,20]

source = "abcdefgh"
target = "acdeeghh"
original = ["bcd","fgh","thh"]
changed = ["cde","thh","ghh"]
cost = [1,3,5]

source = "aaaddcaaccbabaaccbabbaadcccadbaacbddbaccabddbdbaaddbbacbddddbbdbccaadcaccacdbcbddbacabadaaccbadbbdbc"
target = "abaddcabcdbabcbadcaccaadabbadddbcacaaabdabbdcbbdbcbaaabbbcddcbddcbccadacddcbdcbacadbbadbdabcbadbbdac"
original = ["ddddb","dccbb","dadac","dbdbb","ddbacabadaac","bcbccdcadabd","dacabcdaacca","dcdadacacbbd","dcccadbaacbddbacc","dcdcbccdccdbaaaac","bbbcccdbcdcadaabc","bccaadcaccacdb","bbcabcbcbaddbd","dbadadaddcddad","badaddbcddacca","bc","da","cb","ddbdbaaddbbac","dbcadcdbabddd","abdadacbbbcca","adaaabcabdbcc","caaccbabaaccbabba","abaadddbaaccbbacc","bbddaaadcbccccbac","cdbdbddaadbbbdbdd","bcbdaabaddbdcdcaa","aa","cb","dd"]
changed =  ["dccbb","dadac","dbdbb","bcddc","bcbccdcadabd","dacabcdaacca","dcdadacacbbd","acadbbadbdab","dcdcbccdccdbaaaac","bbbcccdbcdcadaabc","dabbadddbcacaaabd","bbcabcbcbaddbd","dbadadaddcddad","badaddbcddacca","dcbccadacddcbd","da","cb","ac","dbcadcdbabddd","abdadacbbbcca","adaaabcabdbcc","bdcbbdbcbaaab","abaadddbaaccbbacc","bbddaaadcbccccbac","cdbdbddaadbbbdbdd","bcbdaabaddbdcdcaa","cabcdbabcbadcacca","cb","dd","ba"]
cost = [67,56,64,83,100,73,95,97,100,98,20,92,58,70,95,77,95,93,69,92,77,53,96,68,83,96,93,64,81,100]
#2405



sol = Solution()
print(sol.minimumCost(source, target, original, changed, cost))

print("aa" in original)
print("ba" in changed)