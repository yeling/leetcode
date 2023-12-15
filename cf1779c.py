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

def main(n, m, nums):
    pre = [0] * n
    pre[0] = nums[0]
    for i in range(1,n):
        pre[i] = pre[i - 1] + nums[i]
    
    ans = 0
    m -= 1
    target = pre[m]
    if nums[m] > 0 and n > 1:
        ans = 1
        target -= 2 * nums[m]
    diff = 0
    # print(pre)
    stack = PriorityQueue()
    for i in range(m-1,-1,-1):
        stack.put(-nums[i])
        if pre[i] < target:
            ans += 1
            temp = -stack.get()
            diff += -2*temp
            target += -2*temp
        
    
    for i in range(m+1, n):
        stack.put(-nums[i])
        if pre[i] + diff < target:
            ans += 1
            temp = -stack.get()
            diff += -2*nums[i]
    print(ans)
    return 

# n = 10
# m = 4
# s = "345875723 -48 384678321 -375635768 -35867853 -35863586 -358683842 -81725678 38576 -357865873"
# nums = list(map(int,s.split()))
# main(n, m, nums)

caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    nums = li()
    main(n, m, nums)

   
