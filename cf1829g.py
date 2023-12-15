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

start = set()
end = set()
ma = 2023
s = 1
zone = []
pos = [[0]*ma for _ in range(ma)]
for i in range(1,ma):
    start.add(s)
    end.add(s + i - 1)
    zone.append((s,s+i-1))
    for j in range(i):
        pos[i][j] = s + j + 1
    s += i
# print(start)
# print(end)
# print(zone)
def main(n):
    layer = 0
    index = 0
    for i in range(len(zone)):
        if n >= zone[i][0] and n <= zone[i][1]:
            layer = i + 1
            index = n - zone[i][0] + 1
            break
    print(layer)
    ans = 0
    stack.append()
    while layer > 0:
        


    
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    main(n)
   
