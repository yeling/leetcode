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
    pos = [-1] * 26
    for i in range(n):
        if pos[ord(s[i]) - 97] == -1:
            pos[ord(s[i]) - 97] = i
        elif (i - pos[ord(s[i]) - 97])%2 == 1:
            print('No')
            return
        else:
            pos[ord(s[i]) - 97] = i
    
    print('Yes')
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    main(n, s)
   
