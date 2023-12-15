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

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main(q, qs):
    l = 1
    r = INF
    ans = []
    for v in qs:
        if v[0] == 1:
            a,b,n = v[1:]
            adopt = 0
            if r > n*a - (n-1) * b:
                r = n*a - (n-1) * b
                adopt = 1
            
            if(n > 1):
                if l < (n-1)*a - (n-2) * b + 1:
                    l = (n-1)*a - (n-2) * b + 1
                    adopt = 1     
            # print(l, r)
            ans.append(adopt)            
        else:
            a,b = v[1:]
            if (r - b)//(a - b) <= 1 and r - l <= a:
                ans.append((r - b)//(a - b))
            elif r - l <= a - b:
                ans.append((r - b)//(a - b))
            else:
                ans.append(-1)

    print(*ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    q = int(input())
    qs = []
    for _ in range(q):
        qs.append(li())
    main(q, qs)
   
