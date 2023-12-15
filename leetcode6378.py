
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
    
class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        g = [list() for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        
        def shortest_path(s, end, price):
            import heapq
            que = []
            d = [10**15] * n
            d[s] = price[s]
            heapq.heappush(que, (price[s], s))
            while len(que) != 0:
                cost, v = heapq.heappop(que)
                if d[v] < cost: continue

                for i in range(len(g[v])):
                    e = g[v][i]
                    if d[e] > d[v] + price[e]:
                        d[e] = d[v] + price[e]
                        heapq.heappush(que, (d[e], e))
            return d[end]
        def calTotal(vis):
            #计算
            global ans
            newPrice = price[:]
            for i,v in enumerate(vis):
                if v == True:
                    newPrice[i] //= 2
            
            print(newPrice, vis)
            total = 0
            for u,v in trips:
                total += shortest_path(u,v,newPrice)
            ans = min(ans, total)
            return total
        
        global ans
        ans = INF
        # print(calTotal(price))
        vis = [False] * n
        #flag [True, False]
        def dfs(u, fa, flag, vis):
            calTotal(vis)
            for v in g[u]:
                if v != fa:
                    if flag[0] == True and flag[1] == False:
                        #不选
                        nextflag = [False, False]
                        dfs(v, u, nextflag,vis)
                        #选择
                        vis[v] = True
                        nextflag = [False, True]
                        dfs(v, u, nextflag,vis)
                        vis[v] = False

                    elif flag[0] == False and flag[1] == False:
                        #选择
                        vis[v] = True
                        nextflag = [False, True]
                        dfs(v, u, nextflag,vis)
                        vis[v] = False
                    elif flag[0] == False and flag[1] == True:
                        #不选
                        nextflag = [True, False]
                        dfs(v, u, nextflag,vis)
            
        
        vis[0] = True
        dfs(0, -1, [False, True], vis)
        vis[0] = False
        dfs(0, -1, [True, False], vis)
        


        return ans
    

n = 4
edges = [[0,1],[1,2],[1,3]]
price = [2,2,10,6]
trips = [[0,3],[2,1],[2,3]]
sol = Solution()
print(sol.minimumTotalPrice(n, edges, price, trips))
