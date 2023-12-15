
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
    # 495 / 663 
    # 556 / 663 
    def maximumSum(self, nums: List[int]) -> int:    
        n = len(nums)
        # 一个数字处以 4 9 25 。。。 剩下来的值，
        # 如果两个数字剩下来的相同，他们的乘积就是完全平方数
        core = defaultdict(list)
        for i in range(n):
            curr = i + 1
            for j in range(2, int(sqrt(n)) + 1):
                if curr < j:
                    break
                while curr % (j * j) == 0:
                    curr //= (j * j)
            core[curr].append(i)
        # print(core)
        ans = 0
        for k in core:
            temp = sum(nums[v] for v in core[k])
            ans = max(ans, temp)


        return ans
    
nums = [8,7,3,5,7,2,4,9]
nums = [1,100,100,1]
nums = [81473,18654,204199312,737158873,801267106,85412399,152001707,322860171,562717602,557578408,649205355,243332471,614146787,260712470,472960947,567346135,499087780,704617573,176522854,657123785,518675803,899926948,189728112,15739370,867361353,791903552,512788957,923045616,549793550,460415042,687985197,116257175,451414174,125320943,601318119,24779116]
sol = Solution()
print(sol.maximumSum(nums))
