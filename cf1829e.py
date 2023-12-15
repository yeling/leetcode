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
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main2(n,m, grid):
    n = len(grid)
    m = len(grid[0])
    #查找father
    def find(father, u):
        if father[u] != u:
            father[u] = find(father,father[u])
        return father[u]
    #合并
    def join(father, u, v):
        fu = find(father,u)
        fv = find(father,v)
        if fu != fv:
            father[fu] = fv
    
    father = list(range(n*m))
    vis = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and vis[i][j] == False:
                dirs = [[1,0], [-1,0],[0,1],[0,-1]]
                for k in dirs:
                    dx = i + k[0]
                    dy = j + k[1]
                    if 0 <= dx < n and  0 <= dy < m and vis[dx][dy] == False and grid[dx][dy] > 0:
                        join(father, i * m + j, dx * m + dy)
                        vis[i][j] = True
            vis[i][j] = True

    rootMap = defaultdict(int)
    ans = 0
    for i in range(len(father)):
        fa = find(father, father[i])
        rootMap[fa] += grid[i//m][i%m]
        ans = max(ans, rootMap[fa])
    print(ans)
    return 

def main(n,m, grid):
    n = len(grid)
    m = len(grid[0])
    #查找father
    def find(father, u):
        if father[u] != u:
            father[u] = find(father,father[u])
        return father[u]
    #合并
    def join(father, u, v):
        fu = find(father,u)
        fv = find(father,v)
        if fu != fv:
            father[fu] = fv
    
    father = list(range(n*m))
    # vis = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                dirs = [[1,0], [-1,0],[0,1],[0,-1]]
                for k in dirs:
                    dx = i + k[0]
                    dy = j + k[1]
                    if 0 <= dx < n and  0 <= dy < m and grid[dx][dy] > 0:
                        join(father, i * m + j, dx * m + dy)
    rootMap = defaultdict(int)
    ans = 0
    for i in range(len(father)):
        fa = find(father, father[i])
        rootMap[fa] += grid[i//m][i%m]
        ans = max(ans, rootMap[fa])
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    grid = []
    for _ in range(n):
        grid.append(li())
    main(n,m, grid)
   
