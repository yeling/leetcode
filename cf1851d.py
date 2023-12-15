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

def solve2(n, nums):
    if nums[-1] > (1 + n) * n // 2:
        print(NO)
        return
    diff = []
    
    for i in range(1, n - 1):
        diff.append(nums[i] - nums[i - 1])
    
    cnt = [0]*(n + 1)
    left = []
    for v in diff:
        if v > n:
            left.append(v)
            if v >= 2 * n:
                print(NO)
                return
        else:
            if cnt[v] > 0:
                left.append(v)
            else:
                cnt[v] += 1
    miss = []
    for i in range(1,n + 1):
        if cnt[i] == 0:
            miss.append(i)
    
    print('diff', diff, 'left',left, 'miss', miss)

    # 1开头中间空缺
    if nums[0] == 1 and len(miss) == 3 and len(left) == 1 and miss[-1] + miss[-2] == left[0]:
        print(YES)
        return
    # 1开头尾部空缺
    if nums[0] == 1 and len(miss) == 2 and len(left) == 0 and miss[-1] + nums[-1] == (n + 1)*(n)//2:
        print(YES)
        return
    # 其他值开头

    if nums[0] != 1:
        #丢掉第一个元素
        if len(left) == 0 and len(miss) == 2 and miss[0] + miss[1] == nums[0]:
            print(YES)
            return
        #丢掉中间元素
        if len(left) == 1 and nums[0] in miss and sum(miss) == left[0] + nums[0]:
            print(YES)
            return
        #丢掉最后一个原色
        if len(left) == 1 and nums[0] in miss and sum(miss) == left[0] + nums[0]:
            print(YES)
            return
        if len(left) == 0 and nums[0] in miss and ((n + 1)*(n)//2 - nums[-1]) in miss:
            print(YES)
            return
    
    print('diff', diff, 'left',left, 'miss', miss)
    print(NO)
        

def solve(n, nums):
    if nums[-1] > (1 + n) * n // 2:
        print(NO)
        return
    diff = []
    
    for i in range(1, n - 1):
        diff.append(nums[i] - nums[i - 1])
    
    cnt = [0]*(n + 1)
    left = []

    s = (n + 1)*n//2
    if nums[-1] != s and s - nums[-1] >= 0 and s - nums[-1] <= n:
        cnt[s - nums[-1]] += 1

    for v in diff:
        if v > n:
            left.append(v)
            if v >= 2 * n:
                print(NO)
                return
        else:
            if cnt[v] > 0:
                left.append(v)
            else:
                cnt[v] += 1
    miss = []
    for i in range(1,n + 1):
        if cnt[i] == 0:
            miss.append(i)
    
    if nums[-1] == s:
        print('diff', diff, 'left',left, 'miss', miss)
        #第一个缺少
        if len(left) == 0 and len(miss) == 2 and sum(miss) == nums[0]:
            print(YES)
            return
        #中间缺少
        if len(left) == 1 and len(miss) == 3 and sum(miss) == left[0] + nums[0]:
            print(YES)
            return
    else:
        # 最后一项不存在，只有第一个可能不存在
        if len(miss) == 1 and miss[0] == nums[0] and len(left) == 0:
            # print('diff', diff, 'left',left, 'miss', miss)
            print(YES)
            return
        
        # print('cnt', cnt)
    # print('diff', diff, 'left',left, 'miss', miss)
    print(NO)







    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve2(n, nums)

   
