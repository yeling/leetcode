
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
    # 76 / 210
    # AC
    def maxProfit2(self, prices: List[int]) -> int:
        # 0 不操作 1 买入 2 卖出 
        # dp[i][j] i价格，当前持有的价格，j状态，值为收益
        cnt = 10 ** 3 + 1
        # cnt = 5
        first = None
        second = [[-1] * 3 for _ in range(cnt)]
        three = None
        for v in prices:
            three = [[-1] * 3 for _ in range(cnt)]
            for i in range(cnt):
                three[i][0] = max(three[i][0], second[i][0])
                three[i][1] = max(three[i][1], second[i][1])
                three[i][2] = max(three[i][2], second[i][2])

                three[v][1] = max(three[v][1], second[i][0], 0)
                if first != None:
                    three[v][1] = max(three[v][1], first[i][2])

                if second[i][1] != -1:
                    three[v][2] = max(three[v][2], v - i + second[i][1])

            first = second
            second = three
            # print(v)
            # print(first)
            # print(second)
            # print(three)
        ans = 0
        for i in range(cnt):
            for j in range(3):
                ans = max(ans, three[i][j])
                ans = max(ans, second[i][j])
        return ans
    
    def maxProfit(self, prices: List[int]) -> int:
        # 0 不操作 1 买入 2 卖出 
        # 将操作转化为持有
        # 0 持有 1 不持有，处于冷冻期 2 不持有，不处于冷冻期 
        # dp[i][j] i价格，当前持有的价格，j状态，值为收益
        cnt = 10 ** 3 + 1
        # cnt = 5
        first = None
        second = [[-1] * 3 for _ in range(cnt)]
        three = None
        for v in prices:
            three = [[-1] * 3 for _ in range(cnt)]
            for i in range(cnt):
                three[i][0] = max(three[i][0], second[i][0])
                three[i][1] = max(three[i][1], second[i][1])
                three[i][2] = max(three[i][2], second[i][2])

                three[v][1] = max(three[v][1], second[i][0], 0)
                if first != None:
                    three[v][1] = max(three[v][1], first[i][2])

                if second[i][1] != -1:
                    three[v][2] = max(three[v][2], v - i + second[i][1])

            first = second
            second = three
            # print(v)
            # print(first)
            # print(second)
            # print(three)
        ans = 0
        for i in range(cnt):
            for j in range(3):
                ans = max(ans, three[i][j])
                ans = max(ans, second[i][j])
        return ans
    
prices = [1,2,3,0,2]
# prices = [1]
# prices = [1,2,4]
# prices = [1,4,2]
sol = Solution()
print(sol.maxProfit(prices))
