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
    n = len(s)
    for i in range(1,n):
        for j in range(i + 1, n):
            if s[:i] <= s[i:j] and s[j:] <= s[i:j]:
                print(s[:i], s[i:j], s[j:])
                return
            elif s[:i] >= s[i:j] and s[j:] >= s[i:j]:
                print(s[:i], s[i:j], s[j:])
                return
    print(":(")
    return 

caseNum = int(input())
for i in range(0, caseNum):
    s = input()
    main(s)
   
