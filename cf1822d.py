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

def check(arr):
        # print('check', arr)
        n = len(arr)
        cache = set()
        s = 0
        for v in arr:
            s += v
            s%= n
            if s in cache:
                return False
            cache.add(s)
            # print(s, cache)

        return len(cache) == n

def test(n):
    for v in permutations(range(1,n+1)):
        if check(v):
            print(v)


    return 

def main(n):
    if n == 1:
        print(1)
        return
    if n%2 == 1:
        print(-1)
        return
    
    ans = [0] * n
    ans[0] = n
    ans[-1] = 1
    l = 2
    r = n - 1
    flag = True
    for i in range(n//2 - 1):
        if flag:
            ans[1+i] = r
            ans[-1-i-1] = r - 1
            r -= 2
            flag = False
        else:
            ans[1+i] = l
            ans[-1-i-1] = l + 1
            l += 2
            flag = True
    print(*ans)
    # print(ans, check(ans))
    return 

# test(6)
# test(8)
# main(16)
caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    main(n)
   
