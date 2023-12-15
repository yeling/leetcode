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

def main(n):
    ans = [n]
    while n > 1:
        if n%2 == 1:
            if (n - 1)//2%2 == 1:
                ans.append((n-1)//2)
                n = (n - 1)//2
            else:
                ans.append((n+1)//2)
                n = (n + 1)//2
        else:
            print(-1)
            return
    temp = []
    curr = 1
    for i in range(len(ans)):
        if 2 * curr - 1 == ans[-1-i]:
            temp.append(1)
        elif 2 * curr + 1 == ans[-1-i]:
            temp.append(2)
        curr = ans[-1-i]
    print(len(temp) - 1)
    print(*temp[1:])

    return 

# main(17)
caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    main(n)
   
