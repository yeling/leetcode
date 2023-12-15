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



def solve(n, nums):
    # print(n)
    #dfs
    vis = [False] * (n + 1)
    for i in range(n):
        temp = []
        curr = i + 1
        while vis[curr] == False:
            vis[curr] = True
            temp.append(curr)
            curr = nums[curr - 1]
        if len(temp) > 0:
            ans = []
            for j in range(len(temp)):
                if temp[j] == curr:
                    ans = temp[j:]
                    print(len(ans))
                    print(*ans)
                    return
    return


n = int(input())
nums = li()
solve(n, nums)
