
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue


MOD = 10 ** 9 + 7

class Solution:
    #0到其他节点的最短路径
    #bfs每次把最短路径拿出来，走向其他节点
    #dis 距离矩阵 vis 可见性矩阵
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        vis = [True] * n
        #剩余距离
        dis = [0] * n
        g = defaultdict(set)
        #记录这条边的剩余节点
        cache = defaultdict(int)
        for item in edges:
            item = tuple(item)
            u,v,cnt = item
            # print(u,v,cnt)
            g[u].add((v,item))
            g[v].add((u,item))
            cache[(u,v)] = cnt

        # print(g)
        res = 0
        stack = PriorityQueue()
        #(leftMove,p)
        stack.put((-(maxMoves + 1),0))
        dis[0] = maxMoves
        
        while stack.empty() == False:
            curr = list(stack.get())
            if vis[curr[1]] == False:
                continue

            curr[0] = -curr[0]
            # print(curr, res)
            vis[curr[1]] = False
            res += 1
            curr[0] -= 1
            if curr[0] == 0:
                continue
            
            for v in g[curr[1]]:
                if v[0] < curr[1]:
                    key = (v[0],curr[1])
                else:
                    key = (curr[1],v[0])
                #节点没有走过
                if vis[v[0]] == True:
                    if curr[0] >= v[1][2] + 1:
                        dis[v[0]] = max(dis[v[0]], curr[0] - v[1][2])
                        stack.put((-dis[v[0]], v[0]))
                        res += v[1][2]
                        cache[key] = -1
                    else:
                        res += curr[0]
                        cache[key] = v[1][2] - curr[0]
                else:
                    #节点走过，但是中间点没走完
                    if cache[key] != -1:
                        if cache[key] < curr[0]:
                            res += cache[key]
                            cache[key] = -1
                            #当前节点更优，更新目标节点
                            dis[v[0]] = max(dis[v[0]], curr[0] - cache[key] - 1)
                            stack.put((-dis[v[0]], v[0]))

                        else:
                            res += curr[0]
                            cache[key] = cache[key] - curr[0]        
        return res


edges = [[0,1,10],[0,2,1],[1,2,2]]
maxMoves = 6
n = 3
# edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]]
# maxMoves = 10
# n = 4
# edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]]
# maxMoves = 17
# n = 5

# edges = [[0,3,8],[0,1,4],[2,4,3],[1,2,0],[1,3,9],[0,4,7],[3,4,9],[1,4,4],[0,2,7],[2,3,1]]
# maxMoves = 8
# n = 5

sol = Solution()
print(sol.reachableNodes(edges, maxMoves, n))
