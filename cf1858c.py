# auther yeling
import sys
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from heapq import *
import string
from os import path

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"


# for I/O for local system
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    # sys.stdout = open("output.txt","w")

# For fast I/O
# input = sys.stdin.buffer.readline
# input = sys.stdin.readline
# print = sys.stdout.write

input = lambda: sys.stdin.readline().rstrip()
si = lambda :int(input())
mi = lambda :map(int,input().split())
li = lambda :list(mi())

def solve(n):
    vis = [False] * (n + 1)
    ans = [1]
    vis[1] = True
    i = 2
    while i <= n:
        j = 1
        while i * j <= n and vis[i * j] == False:
            ans.append(i*j)
            vis[i * j] = True
            j *= 2
        i += 1
    print(*ans)
    # print(ans, calc(ans))


    return 
def calc(p):
    n = len(p)
    temp = 0
    for i,v in enumerate(p):
        temp += gcd(v, p[(i + 1 + n)%n])
    # print(temp)
    return temp

def check(n):
    ans = 0
    for p in permutations(range(1,n+1)):
        # print(p)
        p = [1,2,3,4,8,5,10,6,9,7]
        temp = 0
        for i,v in enumerate(p):
            temp += gcd(v, p[(i + 1 + n)%n])
        if temp >= ans:
            ans = temp
            print(ans, p)
    return

# check(7)
# p = [1,2,3,4,8,5,10,6,9,7]
# p = [1, 2, 3, 6, 4, 5, 7]
# print(calc(p))

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    solve(n)

   
