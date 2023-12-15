
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
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        n = len(bucket)
        ma = 0
        for i in range(n):
            if bucket[i] == 0:
                if vat[i] > 0:
                    ma = max(ma, vat[i] + 1)
            else:
                ma = max(ma, (vat[i] - 1)//bucket[i] + 1)
        
        ans = ma
        for i in range(1,ma+1):
            curr = i
            for j in range(n):
                temp = (vat[j] - 1)//i + 1 - bucket[j]
                if temp > 0:
                    curr += temp
                # print(i, j, temp, ans)
            ans = min(ans,curr)


        return ans
    
bucket = [1,3]
vat = [6,8]
bucket = [0]
vat = [0]
sol = Solution()
print(sol.storeWater(bucket, vat))
