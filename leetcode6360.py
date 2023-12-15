
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

class Solution:
    def distance2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            for j in range(n):
                if nums[i] == nums[j]:
                    ans[i] += abs(i - j)
        return ans
    
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        cnt = defaultdict(int)
        dis = defaultdict(list)
        for i,v in enumerate(nums):
            cnt[v] += 1
            dis[v].append(i)
        # print(cnt, dis)
        for k in list(dis.keys()):
            temp = dis[k]
            preTemp = [0]*(len(temp) + 1)
            for i,v in enumerate(temp):
                preTemp[i + 1] = preTemp[i] + v
            dis[k] = preTemp
        # print(cnt, dis)
        currCnt = defaultdict(int)
        for i,v in enumerate(nums):
            pre = currCnt[v]
            # print(i, v, pre)
            ans[i] = pre * i - dis[v][pre] 
            if pre + 1 < cnt[v]:
                ans[i] += dis[v][-1] - dis[v][pre + 1] - (cnt[v] - pre - 1) * i
            currCnt[v] += 1
            


        return ans
    
nums = [1,3,1,1,2]
nums = [0,5,3]
sol = Solution()
print(sol.distance(nums))
