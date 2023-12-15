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

def solve(s):
    n = len(s)
    last = s[0]
    for i in range(0,n//2):
        if s[i] != last:
            print(YES)
            return 
    print(NO)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    s = input()
    solve(s)

   
