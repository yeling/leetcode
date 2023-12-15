
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
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:  
        print(bin(19))  
        coins.sort()
        n = len(coins)
        ans = [1]
        i = 1
        while i < target:
            ans.append(i << 1)
            i <<= 1
        print(ans) 
        l = 0
        r = 0
        pre = 0
        ret = []
        
        while l < n and r < len(ans):
            while l < n and coins[l] <= ans[r]:
                pre += coins[l]
                l += 1
            if pre + ans[r]//2 < ans[r]:
                ret.append(ans[r])
            else:
                pre -= ans[r]
            r += 1
            print(pre, ret)

        

        print(ret)

        return len(ret)
    
coins = [1,4,10]
target = 19
coins = [1,4,10,5,7,19]
target = 19
coins = [1,1,1]
target = 20
sol = Solution()
print(sol.minimumAddedCoins(coins, target))
