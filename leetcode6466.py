
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

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:   
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                if gcd(int(str(nums[i])[0]),nums[j]%10) == 1:
                    ans += 1

        return ans
    
nums = [2,5,1,4]
nums = [11,21,12]
nums = [31,25,72,79,74]
sol = Solution()
print(sol.countBeautifulPairs(nums))
