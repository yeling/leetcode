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
    if s[0] == '0':
        print(0)
        return
    c = s.count('?')
    ans = 0
    if s[0] == '?':
        ans = 9 * pow(10, c - 1)
    else:
        ans = pow(10,c)
    print(int(ans))
    return 

caseNum = int(input())
for i in range(0, caseNum):
    s = input()
    main(s)
   
