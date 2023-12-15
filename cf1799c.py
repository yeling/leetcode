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

def main(s):
    stack = PriorityQueue()
    for v in s:
        stack.put(v)
    ans = [0] * len(s)
    pos = 0
    while stack.empty() == False:
        a = stack.get()
        ans[-pos-1] = a
        if stack.empty() == False:
            b = stack.get()
            ans[pos] = b
        
        pos += 1
    print(''.join(ans))

    return 

caseNum = int(input())
for i in range(0, caseNum):
    s = input()
    main(s)
   
