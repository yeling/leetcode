
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
    def maximumTastiness(self, price: List[int], k: int) -> int:
        left = 0
        price.sort()
        right = (price[-1] - price[0])//(k - 1)
        n = len(price)
        def check(mid):
            # print('check', mid)
            ans = 0
            start = 0
            while start < n:
                ans += 1
                start = bisect_left(price,price[start] + mid,lo = start + 1)
            return ans
        
        while left <= right:
                # print(left, right)
                mid = left + (right - left)//2
                target = check(mid)
                if target < k:
                    right = mid - 1
                elif target >= k:
                    left = mid + 1    
        return right
    
price = [13,5,1,8,21,2]
k = 3
price = [3,3,3]
k = 2
sol = Solution()
print(sol.maximumTastiness(price, k))
