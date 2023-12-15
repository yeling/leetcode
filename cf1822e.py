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

def main2(n, s):
    if n%2 == 1:
        print(-1)
        return 
    l = n//2
    ans = 0
    #dp[i][j] = 1 a,a 数量，a,b数量
    dp = [[0]*26 for _ in range(26)]
    for i in range(l):
        dp[ord(s[i]) - 97][ord(s[-1-i]) - 97] += 1
    # print(dp)
    ma = 0
    value = 0
    for i in range(26):
        if dp[i][i] > value:
            value = dp[i][i]
            ma = i

    for i in range(26):
        #step 1 两两对消，从最多的开始消除
        i = (i + ma)%26
        if dp[i][i] != 0:
            for j in range(26):
                if i == j or dp[j][j] == 0:
                    continue
                diff = min(dp[j][j],dp[i][i])
                dp[i][j] += diff
                dp[j][i] += diff
                dp[i][i] -= diff
                dp[j][j] -= diff
                ans += diff
                if dp[i][i] == 0:
                    break
        #step2 找没有i的消
        if dp[i][i] != 0:
            for j in range(0, 26):
                if i == j:
                    continue
                for k in range(0,26):
                    if i == k or j == k or dp[j][k] == 0:
                        continue
                    diff = min(dp[j][k],dp[i][i])
                    dp[j][i] += diff
                    dp[i][k] += diff
                    dp[i][i] -= diff
                    dp[j][k] -= diff
                    ans += diff
                    if dp[i][i] == 0:
                        break
        #step3
        if dp[i][i] != 0:
            print(-1)
            return
        
    print(ans)
                    
    return 


def main(n, s):
    if n%2 == 1:
        print(-1)
        return 
    l = n//2
    ans = 0
    #dp[i][j] = 1 a,a 数量，a,b数量
    dp = [[0]*26 for _ in range(26)]
    for i in range(l):
        dp[ord(s[i]) - 97][ord(s[-1-i]) - 97] += 1
    # print(dp)
    # (value, index)
    stack = PriorityQueue()
    for i in range(26):
        if dp[i][i] > 0:
            stack.put((-dp[i][i],i))
    #step 1 两两对消，从最多的两组开始消除
    while not stack.empty():
        a = stack.get()
        if stack.empty():
            break
        b = stack.get()
        i = a[1]
        j = b[1]
        diff = min(dp[j][j],dp[i][i])
        dp[i][j] += diff
        dp[j][i] += diff
        dp[i][i] -= diff
        dp[j][j] -= diff
        ans += diff
        if dp[i][j] != 0:
            stack.put((-dp[i][i],i))
    #step2 最后一组
    for i in range(26):
        if dp[i][i] != 0:
            for j in range(0, 26):
                if i == j:
                    continue
                for k in range(0,26):
                    if i == k or j == k or dp[j][k] == 0:
                        continue
                    diff = min(dp[j][k],dp[i][i])
                    dp[j][i] += diff
                    dp[i][k] += diff
                    dp[i][i] -= diff
                    dp[j][k] -= diff
                    ans += diff
                    if dp[i][i] == 0:
                        break
            #step3
            if dp[i][i] != 0:
                print(-1)
                return
        
    print(ans)
                
                    
    return 
# n = 12
# s = 'dcbcaebacccd'
# print(ord('a'))
# main(n, s)
caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    main(n, s)
   
