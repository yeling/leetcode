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

def solve2(s, n):
    pos = []
    sn = len(s)
    for i in range(sn - 1):
        if s[i] > s[i + 1]:
            pos.append(i)
    if len(pos) < sn:
        add = sn - len(pos)
        pos = pos + list(range(sn - 1, sn - 1 - add , -1))
    # print(pos)
    left = 0
    right = sn - 1
    target = n
    while left <= right:
            mid = left + (right - left)//2
            curr = (sn + sn - mid) * (mid + 1)// 2
            if target <= curr:
                right = mid - 1
            elif target > curr:
                left = mid + 1
    # print(s, left)
    vis = [True] * sn
    for i in range(left):
        vis[pos[i]] = False
    dst = []
    for i in range(sn):
        if vis[i]:
            dst.append(s[i])
    left -= 1
    temp = n - (sn + (sn - left)) * (left + 1)//2 - 1
    # print(s, left, dst, temp)
    return dst[temp]
    # return ''
#单调栈
def solve(s, n):
    pos = []
    sn = len(s)
    #(index, v)
    stack = []
    for i in range(sn):
        while len(stack) > 0 and stack[-1][1] > s[i]:
            curr = stack.pop()
            pos.append(curr[0])
        stack.append((i,s[i]))
    for v in stack[::-1]:
        pos.append(v[0])   
    # print(pos)
    step = sn
    cnt = 0
    vis = [True] * sn
    for i in range(sn):
        cnt += step
        step -= 1
        if cnt >= n:
            break
        else:
            vis[pos[i]] = False   
    dst = []
    for i in range(sn):
        if vis[i]:
            dst.append(s[i])
    # print(dst[-1 - (cnt - n)])
    # print(s, dst, cnt - n)
    return dst[-1 - (cnt - n)]
    # return ''

caseNum = int(input())
ans = []
for i in range(0, caseNum):
    s = input()
    n = int(input())
    ans.append(solve(s, n))
print(''.join(ans))
   
