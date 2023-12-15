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

def solve2(n, grid):
    dp = [[0]*n for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if i - 1 >= 0:
                dp[i][j] += dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i - 1][j - 1]
                if j + 1 < n:
                    dp[i][j] += dp[i - 1][j + 1]

            curr = int(grid[i][j]) + dp[i][j]%2        
            ans += curr%2
            dp[i][j] += curr%2
            print(i, j , ans)
    
    print(dp)
    print(ans)

    return 

def solve3(n, grid):

    dp = []
    for _ in range(n):
        dp.append([[0]*3 for _ in range(n)])
    # 0, 1, 2
    ans = 0
    for i in range(n):
        for j in range(n):
            if i - 1 >= 0:
                dp[i][j][1] += dp[i - 1][j][1]
                if j - 1 >= 0:
                    dp[i][j][0] += dp[i - 1][j - 1][0]
                if j + 1 < n:
                    dp[i][j][2] += dp[i - 1][j + 1][2]

            curr = int(grid[i][j]) + sum(dp[i][j])%2        
            ans += curr%2
            if curr%2 == 1:
                dp[i][j][0] += curr%2
                dp[i][j][1] += curr%2
                dp[i][j][2] += curr%2
            print(i, j, ans)
            
    print( dp)
    print(ans)

    return 

# 记录 x + y 的值， x - y 的值
# dp[i][j] = dp[i - 1][j] + cache1[x + y] + cache2[x - y]
# dp[i][j] += curr%2
def solve(n, grid):
    dp = [[0]*n for i in range(n)]
    ans = 0
    # x + y
    cache1 = defaultdict(int)
    # x - y
    cache2 = defaultdict(int)
    for i in range(n):
        for j in range(n):
            if i - 1 >= 0:
                dp[i][j] += dp[i - 1][j]
            
            dp[i][j] += cache1[i + j]
            dp[i][j] += cache2[i - j]
            curr = int(grid[i][j]) + dp[i][j]      
            ans += curr%2
            cache1[i + j] += curr%2
            cache2[i - j] += curr%2
            dp[i][j] += curr%2
            # print(i, j , ans)
    
    # print(dp)
    print(ans)
    return

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(input())
    solve(n, grid)

   
