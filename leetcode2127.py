
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
    # 45 / 98 
    # 47 / 98 
    # 52 / 98
    def maximumInvitations(self, favorite: List[int]) -> int: 
        n = len(favorite)
        cnt = [0] * n
        mark = [False] * n
        stack = deque()
        ind = [0] * n
        for v in favorite:
            ind[v] += 1
        for i,v in enumerate(ind):
            if v == 0:
                stack.append(i)
        #拓扑排序找环,入度为0的开始遍历
        while len(stack) > 0:
            x = stack.popleft()
            y = favorite[x]
            # print(x, y, stack, ind)
            ind[y] -= 1
            #入读为0的计算之后，出现新的入度为0的节点加入队列
            if ind[y] == 0:
                stack.append(y)
        # 计算环的长度
        for i,v in enumerate(ind):
            if v > 0 and mark[i] == False:
                c = 1
                curr = favorite[i]
                while curr != i:
                    c += 1
                    mark[curr] = True
                    curr = favorite[curr]
                cnt[i] = c
                curr = favorite[i]
                while curr != i:
                    cnt[curr] = c
                    curr = favorite[curr]

        # print(mark, cnt, stack, ind)

        # step2 从环上节点出发，计算树的深度
        depth = [0] * n
        g = [[] for _ in range(n)]
        for i,v in enumerate(favorite):
            g[v].append(i)
        def dfs2(root):
            # print(root)
            curr = 0
            for v in g[root]:
                if ind[v] == 0:
                    dfs2(v)
                    curr = max(curr, depth[v])
            depth[root] = curr + 1
            return 
        for i,v in enumerate(ind):
            if v > 0:
                dfs2(i)
        # print(depth)
        # 计算结果
        # 环长尾2的，一条直线
        # 环长大于2的，一桌取最大
        ans = 0
        two = 0
        for i in range(n):
            if ind[i] > 0:
                if cnt[i] == 2:
                    two = two + depth[i] + depth[favorite[i]]
                    # print(i, two)
                else:
                    ans = max(ans, cnt[i])

        return max(ans, two//2)
    
favorite = [2,2,1,2]
# favorite = [3,0,1,4,1]
# favorite = [1,0,0,2,1,4,7,8,9,6,7,10,8]
favorite = [1,0,3,2,5,6,7,4,9,8,11,10,11,12,10]
favorite = [6,4,4,5,0,3,3]
# favorite = [7,12,17,9,0,7,14,5,3,15,6,14,10,14,10,1,1,4]
# for i,v in enumerate(favorite):
#     print(i, v)

sol = Solution()
print(sol.maximumInvitations(favorite))
