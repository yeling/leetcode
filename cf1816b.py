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

def check(ans):
        dp = [[INF] * n for _ in range(2)] 
        dp[0][0] = ans[0][0]
        for i in range(2):
            for j in range(n):
                if j + 1 < n:
                    sign = 1
                    if (i + j + 1)%2 == 1:
                        sign = -1
                    dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + sign * ans[i][j+1])
                if i + 1 < 2:
                    sign = 1
                    if (i + j + 1)%2 == 1:
                        sign = -1
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + sign * ans[i + 1][j])
        return dp[1][n - 1]

def main(n):
    ans = [[0] * n for _ in range(2)]
    left = 1
    right = 2*n - 2
    ans[0][0] = 2*n
    ans[1][n-1] = 2*n -1
    i = 0
    flag = True
    for i in range(n - 1):
        if flag == True:
            ans[1][i] = left
            ans[0][i + 1] = left + 1
            left += 2
            flag = False
        else:
            ans[1][i] = right - 1
            ans[0][i + 1] = right
            right -= 2
            flag = True
    for v in ans:
        print(*v)
    # print(*ans)
    # print(check(ans))
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    main(n)
   
