
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
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def minOperations2(self, nums: List[int], target: int) -> int:
        #记录每个数位上为1的，对应的数字个数
        cnt = [0]*33
        for v in nums:
            for i in range(32):
                if (v &(1 << i)) != 0:
                    cnt[i] += 1
        # print(cnt)
        ans = 0
        for i in range(32):
            # i数位使用了1
            if (target & ( 1 << i)) != 0:
                cnt[i] -= 1
            # i位不够了，前面借一位（借位需要操作1），每一位最小位-2，前面借一位是足够使用的
            # i位有多余的，凑给前面一位
            if cnt[i] < 0: 
                ans += 1
                cnt[i + 1] -= 1  
            else:
                cnt[i + 1] += cnt[i]//2
            # print(cnt, ans)   
        if cnt[32] == -1:
            return -1   

        return ans
    #1.记录每个数位上为1的，对应的数字个数
    #2.对target从低位到高为进行计算
    #  i数位使用了1， cnt[i] -= 1
    #  统计的i位不够了，前面借一位（借位需要操作1），每一位最小为-2，前面借一位是足够使用的
    #  i位有多余的，凑给前面一位
    def minOperations(self, nums: List[int], target: int) -> int:
        #记录每个数位上为1的，对应的数字个数
        cnt = [0]*33
        for v in nums:
            cnt[len(bin(v)[2:]) - 1] += 1
        print(cnt)
        ans = 0
        for i in range(32):
            # i数位使用了1
            if (target & ( 1 << i)) != 0:
                cnt[i] -= 1
            # i位不够了，前面借一位（借位需要操作1），每一位最小位-2，前面借一位是足够使用的
            # i位有多余的，凑给前面一位
            if cnt[i] < 0: 
                ans += 1
                cnt[i + 1] -= 1  
            else:
                cnt[i + 1] += cnt[i]//2
            # print(cnt, ans)   
        if cnt[32] == -1:
            return -1
        return ans
    
nums = [1,32,1,2]
target = 12
# nums = [1,2,8]
# target = 7
# nums = [1,32,1]
# target = 35

# nums = [16,128,32]
# target = 1

sol = Solution()
print(sol.minOperations(nums, target))
