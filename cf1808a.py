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

def main(l, r):
    ans = 0
    num = l
    for i in range(l, r+1):
        temp = i
        up = 0
        down = 9
        while temp > 0:
            up = max(up, temp%10)
            down = min(down, temp%10)
            temp //= 10
        if up - down > ans:
            num = i
            ans = up - down
        # print(down, up, ans)
        if ans == 9:
            print(i)
            return 
    print(num)


    return 

caseNum = int(input())
for i in range(0, caseNum):
    l,r = li()
    main(l, r)
   
