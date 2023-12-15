
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
    # 1.状态压缩dp,
    # 110011判断子集 110000 gcd(4,5) 000011 gcd(0,1)
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)

        cache = [[1]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                cache[i][j] = gcd(nums[i], nums[j])

        dp = defaultdict(int)
        ans = 0 
        for i in range(3,2**n):
            c = bin(i).count('1')
            if c%2 == 1:
                continue
            j = 0
            k = 0
            while 2 ** j < i:
                while i & ( 1 << j) != (1<<j):
                    j += 1
                k = j + 1
                while (1 << k) < i:
                    if i & ( 1 << k) == (1 << k):
                        dp[i] = max(dp[i], dp[i ^(1<<j)^(1<<k)] + c//2 * cache[j][k])
                    k += 1
                j += 1   

            ans = max(ans, dp[i])    
            # print(i,bin(i), dp[i])
            # print(dp)    
            # print(bin(j))   
        return dp[2**n - 1]

nums = [1,2,3,4,5,6]
# nums = [1,2,3,4]
sol = Solution()
print(sol.maxScore(nums))
