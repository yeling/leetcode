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

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

# mi = lambda: map(int, sys.stdin.buffer.readline().split())
mi = lambda :map(int,input().split())
li = lambda :list(mi())

#暴力用来验证正确性
def solve2(n, k, nums):
    ans = 0
    for i in range(n):
        for j in range(i,n):
            c = Counter(nums[i:j+1])
            # print(c.most_common(1)[0][0])
            if c.most_common(1)[0][1] >= k:
                ans += n - j
                break
        # print(i, ans)
            # if c.most_common(1)
    print(ans)
    return 
#双向滑动的计算
def solve(n, k, nums):
    cache = Counter()
    l = 0
    r = 0
    ans = 0
    while r < n:
        # print(n, r, nums)
        # r向右寻找
        flag = False
        while r < n:
            cache[nums[r]] += 1
            if cache[nums[r]] == k:
                flag = True
                ans += n - r
                r += 1
                break
            r += 1
        if flag == False:
            break
        # print(l, r, ans)
        # l 向右寻找, 如果满足条件 ans += n - r + 1
        while l < r and l < n:
            cache[nums[l]] -= 1
            if cache[nums[l]] == k - 1:
                l += 1
                break
            l += 1
            if flag:
                ans += n - r + 1
            
            
            
    
        # print(l, r, ans)
        
        
        
    print(ans)
    
    return 

n,k = li()
nums = li()
# solve2(n, k, nums)
solve(n, k, nums)
   
