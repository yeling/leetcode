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

def main(n, m, k, a):
    stack = PriorityQueue()
    preCache = defaultdict(int)
    ans = []
    for i in range(n-m+1):
        if i == 0:
            for j in range(m):
                stack.put(a[i+j])
        else:
            stack.put(a[i])
        
        ts = 0
        take = []
        for j in range(k):
            curr = stack.get()
            while preCache[curr] != 0:
                preCache[curr] -= 1
                curr = stack.get()
            ts += curr
            take.append(curr)
        

        

    # print(n,k,d,a)

n,m,k = mi()
a = li() 
main(n,m, k,a)

