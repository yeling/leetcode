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

def main(n, k):
    up = 0
    for i in range(0,n+2):
        if i*(i + 1)//2 > k:
            up = i
            break
    up = up - 1
    left = k - up*(up + 1)//2
    ans = [2] * up
    if len(ans) < n:
        m = -1 - (up - left) * 2
        ans=[m, *ans]
    for i in range(n-up-1):
        ans.append(-999)
    print(*ans)
    # print()
    return 
# main(4,6)
# main(4,7)
# main(4,8)
# main(4,9)
# main(3,2)

caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    main(n, k)
   
