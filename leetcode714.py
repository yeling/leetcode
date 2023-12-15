
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
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #dp [i][j] i 个， j状态 0没有股票，1有股票
        # 买入的价格放入结果中计算
        n = len(prices)
        dp = [0] * 2
        dp[1] = -prices[0]
        for i in range(n):
            next = [0] * 2
            next[0] = max(dp[0], dp[1] + prices[i] - fee, 0)
            next[1] = max(dp[1], dp[0] - prices[i])
            dp = next   
        return max(dp)
    
prices = [1, 3, 2, 8, 4, 9]
fee = 2

# prices = [1,3,7,5,10,3]
# fee = 3
sol = Solution()
print(sol.maxProfit(prices, fee))
