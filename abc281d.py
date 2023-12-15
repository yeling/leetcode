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
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())


def main2(n, k, d, a):
    # print(n,k,d,a)
    ans = -1
    def dfs(index : int, pre:List):
        nonlocal ans 
        if len(pre) == k:
            s = sum(pre)
            if s % d == 0:
                ans = max(ans, s)
            return
        if index == n:
            return
        #select
        pre.append(a[index])
        dfs(index + 1, pre)
        pre.pop()
        #nothing
        dfs(index + 1, pre)
    
    dfs(0,[])
    print(ans)

def main3(n, k, d, a):
    # print(n,k,d,a)
    ans = -1
    @lru_cache(maxsize=None)
    def dfs(index : int, preLen:int , preSum: int):
        nonlocal ans 
        if preLen == k:
            if preSum % d == 0:
                ans = max(ans, preSum)
            return
        if index == n:
            return
        #select
        dfs(index + 1, preLen + 1, preSum + a[index] )
        #nothing
        dfs(index + 1, preLen,preSum )
    
    dfs(0,0,0)
    print(ans)

def main(n, k, d, a):
    # print(n,k,d,a)
    ans = -1

n,k,d = mi()
a = li() 
main(n,k,d,a)

