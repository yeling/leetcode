
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    # 27 / 38 
    # 28 / 38 
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        cache = defaultdict(int)
        for i,v in  enumerate(req_skills):
            cache[v] = i
        n = len(req_skills)
        m = len(people)
        dp = [n + 1] * (1<<n)
        dp[-1] = 0
        vis = [[False] * m ] *(1<<n) 
        for i in range((1<<n) - 1,-1,-1):
            for j,v in enumerate(people):
                if vis[i][j] == False:
                    temp = 0
                    for k in v:
                        temp |= 1 << cache[k]
                    # print(v, temp)  
                    dst = i & ~temp
                    if dp[dst] > dp[i] + 1 or (dp[dst] == dp[i] + 1 and vis[dst].count(True) > vis[i].count(True) + 1):
                        dp[dst] = dp[i] + 1
                        vis[dst] = vis[i][:]
                        vis[dst][j] = True
            # print(i, dp)
            # print(vis)                 
        # print(dp[0])
        ans = []
        for i,v in enumerate(vis[0]):
            if v:
                ans.append(i)
        return ans
    
req_skills = ["mwobudvo","goczubcwnfze","yspbsez","pf","ey","hkq"]
# people = [["java"],["nodejs"],["nodejs","reactjs"]]
people = [[],["mwobudvo"],["hkq"],["pf"],["pf"],["mwobudvo","pf"],[],["yspbsez"],[],["hkq"],[],[],["goczubcwnfze","pf","hkq"],["goczubcwnfze"],["hkq"],["mwobudvo"],[],["mwobudvo","pf"],["pf","ey"],["mwobudvo"],["hkq"],[],["pf"],["mwobudvo","yspbsez"],["mwobudvo","goczubcwnfze"],["goczubcwnfze","pf"],["goczubcwnfze"],["goczubcwnfze"],["mwobudvo"],["mwobudvo","goczubcwnfze"],[],["goczubcwnfze"],[],["goczubcwnfze"],["mwobudvo"],[],["hkq"],["yspbsez"],["mwobudvo"],["goczubcwnfze","ey"]]

req_skills = ["a", "b", "c","d"]
people = [["a","b"], ["c"], ["a", "b", "c"],["a","c", "d"],["b","d"]]


sol = Solution()
print(sol.smallestSufficientTeam(req_skills, people))
