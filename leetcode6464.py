
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
from heapq import *
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

#1.获取所有质数因子
#2.计算可以容纳这些质因子的最大N
def getAllfactor(k):
    fac = []
    i = 2 
    y = k
    while i <= y:
        # print(i,y)
        if y % i == 0:
            fac.append(i)
            y = y // i
            i = 2
        elif i > sqrt(y):
            fac.append(y)
            break
        else:
            i += 1
    return fac

#查找father
def find(father, u):
    if father[u] != u:
        father[u] = find(father,father[u])
    return father[u]
#合并
def join(father, u, v):
    fu = find(father,u)
    fv = find(father,v)
    if fu != fv:
        father[fu] = fv    

#预处理，保存所有数字的质因子
primes = defaultdict(list)
for i in range(1,10**5+1):
    fac = getAllfactor(i)
    primes[i] = fac


class Solution:
    # 919 / 921 个通过测试用例
    # 920 / 921 个通过测试用例 TLE
    # 并查集
    def canTraverseAllPairs2(self, nums: List[int]) -> bool:  
        n = len(nums)
        # ma = max(nums)
        ma = 10 ** 5
        vis = [False] * (ma + 1)
        father = list(range(ma + 1))

        for i in range(n):
            fac = getAllfactor(nums[i])
            # print(fac)
            vis[nums[i]] = True
            for v in fac:
                vis[v] = True
                join(father, v, nums[i])
        
        rootMap = defaultdict(int)
        cnt = 0
        for i in range(len(father)):
            # print(i)
            fa = find(father, father[i])
            rootMap[fa] += 1
        for k in rootMap:
            if vis[k] == True:
                cnt += 1
        if cnt == 1 and len(nums) > 1 and nums[1] == 1:
            return False
        # print(rootMap, cnt)
    
        return cnt == 1

    def canTraverseAllPairs3(self, nums: List[int]) -> bool:  
        n = len(nums)
        ma = 10 ** 5
        vis = [False] * (ma + 1)
        father = list(range(ma + 1))
        if n == 1:
            return True

        for i in range(n):
            fac = getAllfactor(nums[i])
            # print(fac)
            vis[nums[i]] = True
            for v in fac:
                vis[v] = True
                join(father, v, nums[i])
        
        tar = find(father, nums[0])
        for i in range(n):
            curr = find(father, nums[i])
            # print(nums[i], curr, tar)
            if curr != tar or curr == 1:
                return False
        
        return True
    
    def canTraverseAllPairs(self, nums: List[int]) -> bool:  
        n = len(nums)
        ma = 10 ** 5
        vis = [False] * (ma + 1)
        father = list(range(ma + 1))
        if n == 1:
            return True
        #每个质数对应的数字
        prime2num = defaultdict(list)
        for i in range(n):
            for v in primes[nums[i]]:
                prime2num[v].append(nums[i])
        for p in prime2num:
            for v in prime2num[p]:
                join(father, p, v)
    
        tar = find(father, nums[0])
        for i in range(n):
            curr = find(father, nums[i])
            # print(nums[i], curr, tar)
            if curr != tar or curr == 1:
                return False
        
        return True
    
nums = [1,1]
nums = [3,3,6]
# nums = [35,13,42,5,10,42]
# nums = [1,6,6,7,35]
# nums = [36,24,30,10,33,15,35,36,6,26,10,14,30,40,45,42,30,42,40,26,30,40,30,21,14,35,39]
# nums = [42,35,30,35,30,11,21,42,42,30,35,21,40,15,11,15,33,26,35,21,42,15]
sol = Solution()
print(sol.canTraverseAllPairs(nums))
print(sol.canTraverseAllPairs2(nums))