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

def solve(n, nums, k):
    cache = list(zip(nums, range(n)))
    cache.sort()
    diff = [0] * (n + 1)
    # print(cache)
    mi = cache[0]
    if mi[0] > k:
        print(*([0]*n))
        return
    if k%mi[0] == 0:
        diff[0] += k//mi[0]
        diff[mi[1] + 1] -= k//mi[0]
    else:
        c = (k - 3 * mi[0] + mi[0] - 1)//3
        left = k
        if c > 0:
            diff[0] += c
            diff[mi[1] + 1] -= c
            left = k - c * 3
        maPos = -1
        for v,i in cache:
            if v < left:
                maPos = i
            else:
                break
        flag = False
        for i in range(maPos, -1, -1):
            for j in range(maPos, -1, -1):
                if cache[i][0] + cache[j][0] <= left:
                    diff[0] += 1
                    diff[cache[i][1] + 1] -= 1
                    diff[0] += 1
                    diff[cache[j][1] + 1] -= 1
                    flag = True
                    break
            if flag:
                break
        if flag == False:
            diff[0] += 1
            diff[maPos + 1] -= 1
    # print(diff)
    ans = [0] * n
    ans[0] = diff[0]
    for i in range(1,n):
        ans[i] = ans[i - 1] + diff[i]
    print(*ans)


        
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    k = int(input())
    solve(n, nums, k)

   
