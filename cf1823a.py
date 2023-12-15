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

def main(n, k):
    for i in range(0,n+1):
        a = i * ( i - 1) // 2
        temp = n - i
        # print(a, temp)

        b = temp * (temp - 1)//2
        if a + b == k:
            ans = [1]*i + [-1]*temp
            # print(YES, a, b)
            print(YES)
            print(*ans)
            return 
    print(NO)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    main(n, k)

   
