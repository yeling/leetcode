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

def main(n, s):
    # print(s)
    if s.count('R') == n or s.count('L') == n:
        print(-1)
        return 
    for i in range(1,n):
        if s[i] != s[i - 1] and s[i - 1] == 'L':
            print(i)
            return
    print(0)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    main(n, s)
   
