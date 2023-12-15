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

# For fast I/O
# input = sys.stdin.buffer.readline
# input = sys.stdin.readline
# print = sys.stdout.write

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

def solve(n, edges, qs):
    g = [[] for _ in range(n+1)]
    for u,v in edges:
        g[u].append(v)
        g[v].append(u)
    # print(g)
    leaf = [0] * (n + 1)

    @bootstrap
    def dfs(index, f):
        # print(index, leaf)
        if len(g[index]) == 1:
            leaf[index] = 1
            yield 1
        for v in g[index]:
            if v != f:  
                leaf[index] += yield dfs(v, index)
        yield leaf[index] 
    
    g[1].append(0)
    dfs(1,0)
    # print(leaf)
    for x, y in qs:
        print(leaf[x]*leaf[y])
 
 
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    edges = []
    for i in range(1,n):
        edges.append(lint())
    q = int(input())
    qs = []
    for i in range(q):
        qs.append(lint())
    solve(n, edges, qs)


   
