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

def main(n, books):
    # print(n, books)
    a = INF
    b = INF
    c = INF
    for m, s in books:
        t = int(m)
        if s[0] == '1':
            a = min(a, t)
        if s[1] == '1':
            b = min(b, t)
        if s == '11':
            c = min(c, t)
    c = min(c, a + b)
    if c == INF and a == INF or b == INF:
        c = -1
    print(c)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    books = []
    for _ in range(n):
        m, s = input().split()
        books.append([m,s])
    main(n, books)
   
