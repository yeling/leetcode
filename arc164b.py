# auther yeling
import sys
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from heapq import *
import string
from os import path

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

# for I/O for local system
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    # sys.stdout = open("output.txt","w")

# input = lambda: sys.stdin.readline().rstrip()
input = lambda: sys.stdin.readline().rstrip()
sint = lambda :int(input())
mint = lambda :map(int,input().split())
lint = lambda :list(mint())

# --------------------
# 手写栈模板
# 克服py栈太浅的问题
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
# --------------------
#函数头加上@bootstrap
#函数内部return改成yield
#yield True
#yield dfs


# AC 26 WA 20
#  
def solve2(n, m, grid, c):
    time = [0] * (n + 1)
    g = [[] for _ in range(n + 1)]
    for a,b in grid:
        g[a].append(b)
        g[b].append(a)
    c = [0] + c
    
    # dfs
    global t
    t = 1
    @bootstrap
    def dfs(i):
        global t
        for v in g[i]:
            if c[v] != c[i] and time[v] == 0:
                time[v] = t
                t += 1
                ret = yield dfs(v)
                if ret == True:
                    yield True
            elif c[v] == c[i] and time[v] != 0:
                if (time[i] - time[v] + 1)%2 == 1:
                    yield True 
        yield False
    
    for i in range(1,n + 1):
        # print(time)
        if time[i] == 0:
            time[i] = t
            t += 1
            ret = dfs(i)
            if ret == True:  
                # print(time) 
                print(YES)
                return 
    print(NO)
    return 

#查找father
# def find(father, u):
#     if father[u] != u:
#         father[u] = find(father,father[u])
#     return father[u]

def find(father, a):
    acopy = a
    while a != father[a]:
        a = father[a]
    while acopy != a:
        father[acopy], acopy = a, father[acopy]
    return a

#合并
def join(father, u, v):
    fu = find(father,u)
    fv = find(father,v)
    if fu != fv:
        father[fu] = fv

def solve(n, m, grid, c):
    c = [0] + c
    father = list(range(n + 1))
    # 0 - 1 1 - 1联合
    # 如果 0-0， 或者 1-1 在同一个集合中 表示存在答案
    for a,b in grid:
        if c[a] != c[b]:
            join(father, a, b)
    for a,b in grid:
        if c[a] == c[b] and find(father, a) == find(father, b):
            print(YES)
            return
    print(NO)
 
    return
n, m = lint()
grid = []
for _ in range(m):
    grid.append(lint())
nums = lint()
solve(n, m, grid, nums)

