
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
    
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        #1.以0为根节点，一层一层的去求cnt, ans
        #dp推理过程，树形dp
        #ans(a) = sum(a) + sum(b) + cnt(b)
        #ans(b) = sum(b) + sum(a) + cnt(a)
        #ans(a) = ans(b) - cnt(a) + cnt(b)
        #ans(a) = ans(b) - cnt(a) + N - cnt(a)
        #ans(child) = ans(root) - cnt(child) + N - cnd(child)
        g = [list() for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        # print(g)
        #记录每个节点子节点的数目
        cnt = [1] * n #记录每个节点子节点的个数(包含该节点)
        ans = [0] * n #记录每个节点的子节点到该节点的路径距离和
        #求出ans[0] cnt值
        def dfs(child, parent):
            for v in g[child]:
                if v != parent:
                    dfs(v, child)
                    cnt[child] += cnt[v]
                    ans[child] += ans[v] + cnt[v]
            return 
        dfs(0, -1)
        # print(ans, cnt)
        def dfs2(child, parent):
            for v in g[child]:
                if v != parent:
                    ans[v] = ans[child] + n - 2 * cnt[v]
                    dfs2(v, child)
            return
        dfs2(0,-1)
        # print(ans, cnt)
        return ans
    
n = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
sol = Solution()
print(sol.sumOfDistancesInTree(n, edges))
