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
si = lambda :int(input())
mi = lambda :map(int,input().split())
li = lambda :list(mi())

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
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

def solve2(n, nums):
    g = [[] for _ in range(n + 1)]
    cnt = [1]*(n + 1)
    for i,v in enumerate(nums):
        g[v].append(i + 2)
    ans = 0
    @bootstrap
    def dfs(u):
        nonlocal ans
        if len(g[u]) == 0:
            yield
        temp = []
        for v in g[u]:
            yield dfs(v)
            temp.append(cnt[v])
        st = sum(temp)
        mt = max(temp)
        if mt >= st - mt:
            ans += st - mt
            cnt[u] += mt - (st - mt)
        else:
            ans += st//2
            cnt[u] += st%2
        print(u, ans, cnt)
        
        yield

    dfs(1)
    print(ans)
    return 

def solve(n, nums):
    g = [[] for _ in range(n + 1)]
    
    for i,v in enumerate(nums):
        g[v].append(i + 2)
    ans = 0

    sub = [1]*(n + 1)
    @bootstrap
    def dfs1(u):
        if len(g[u]) == 0:
            yield
        for v in g[u]:
            yield dfs1(v)
            sub[u] += sub[v]
        yield
    dfs1(1)
    
    cnt = [0]*(n + 1)
    @bootstrap
    def dfs(u):
        nonlocal ans
        if len(g[u]) == 0:
            yield
        temp = []
        for v in g[u]:
            temp.append([sub[v],v])
        if cnt[u] > 0:
            st = sub[u] - cnt[u]
        else:
            st = sub[u] - 1
        mt = max(temp)
        mt[0] -= cnt[u]
        if mt[0] > st - mt[0]:
            ans += st - mt[0]
            cnt[mt[1]] = st - mt[0]
            yield dfs(mt[1])
        else:
            ans += st//2
            cnt[u] += st%2
        # print(u, ans, cnt)
        
        yield

    dfs(1)
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    # print("case i", i)
    solve(n, nums)

# 5
# 1 1 2 2
# 5
# 1 2 1 3
   
