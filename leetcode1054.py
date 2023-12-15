
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
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:  
        n = len(barcodes)
        ans = [0]*len(barcodes)
        #[cnt,index]
        cache = defaultdict(int)
        for v in barcodes:
            cache[v] += 1
        stack = PriorityQueue()
        for k in cache:
            stack.put((-cache[k], k))
        last = 0
        for i in range(n):
            first = stack.get()
            # print(first)
            if first[1] != last:
                last = first[1]
                ans[i] = first[1]
                # if first[0] + 1 < 0:
                stack.put((first[0] + 1, first[1]))
            else:
                second = stack.get()
                ans[i] = second[1]
                last = second[1]
                # if second[0] + 1 < 0:
                stack.put((second[0] + 1, second[1]))
                stack.put(first)
        
        return ans
    
barcodes = [1,1,1,2,2,2,3,3]
barcodes = [1,1,1,2,2,2,2,2,2,2,3,3]

sol = Solution()
print(sol.rearrangeBarcodes(barcodes))
