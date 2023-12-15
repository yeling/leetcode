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

def main(s):
    n = len(s)
    ans = -1
    for i in range(1,n):
        if s[i] != s[i-1]:
            ans = n - 1
            break
    print(ans)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    s = input()
    main(s)
   
