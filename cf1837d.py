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

def solve(n, s):
    stack = []
    if n%2 == 1 or s.count('(') != n//2:
        print(-1)
        return
    flag = s[0] == '('
    ans = [1] * n
    c = 1
    k = 1
    for i in range(n):
        if len(stack) == 0:
            if s[i] == s[0]:
                c = 1
                stack.append(s[i])
            else:
                k = 2
                c = 2
                stack.append(s[i])
        elif stack[-1] == s[i]:
            stack.append(s[i])
        else:
            stack.pop()
        ans[i] = c
    print(k)
    print(*ans)



    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    solve(n, s)

   
