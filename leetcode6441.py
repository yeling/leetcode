
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 1
        for i in range(2, n + 1):
            temp = i * i
            # print(str(temp))
            ns = str(temp)
            # print(ns)
            # ns = '123456'
            cnt = len(ns)
            for j in range(1, 1<<(cnt-1)):
                last = -1
                arr = []
                for k in range(cnt-1):
                    index = (1<<k) & j
                    if index > 0:
                        if last == -1:
                            arr.append(int(ns[0:k + 1]))
                            last = k
                        else:
                            arr.append(int(ns[last+1:k+1]))
                            last = k
                arr.append(int(ns[last+1:]))
                # print(arr)
                if sum(arr) == i:
                    ans += temp
                    break    
        return ans
    
    nums = range(1,5)
    for i in range(1,len(nums) + 1):
        for v in permutations(nums,i):
            print(v)
    
n = 37
sol = Solution()
print(sol.punishmentNumber(n))
