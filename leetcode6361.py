
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
    def diagonalPrime(self, nums: List[List[int]]) -> int:

        def isPrime(n):
            if(n == 1):
                return False
            m = int(sqrt(n))
            for i in range(2,m + 1):
                if n%i == 0:
                    return False
            return True

        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(n):
                if (i == j or i + j == n - 1) and isPrime(nums[i][j]):
                    ans = max(ans, nums[i][j])

        return ans
    
nums = [[1,2,3],[5,6,7],[9,10,11]]

sol = Solution()
print(sol.diagonalPrime(nums))
