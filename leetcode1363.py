
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
    # 38 / 44 
    def largestMultipleOfThree(self, digits: List[int]) -> str:    
        #0,1,2
        cache = [[] for _ in range(3)]
        s = 0
        for v in digits:
            s += v
            cache[v%3].append(v)
        for i in range(3):
            cache[i].sort()
        digits.sort(reverse=True)
        if s%3 == 0:
            if digits[0] == 0:
                return '0'
            else:
                return ''.join([str(v) for v in digits])
        else:
            dst = []
            if s%3 == 1:
                if len(cache[1]) > 0:
                    dst.append(cache[1][0])
                elif len(cache[2]) > 1:
                    dst.append(cache[2][0])
                    dst.append(cache[2][1])
            elif s%3 == 2:
                if len(cache[2]) > 0:
                    dst.append(cache[2][0])
                elif len(cache[1]) > 1:
                    dst.append(cache[1][0])
                    dst.append(cache[1][1])
            if len(dst) == 0:
                return ''
            else:
                ans = []
                dst = Counter(dst)
                for v in digits:
                    if v in dst and dst[v] > 0:
                        dst[v] -= 1
                    else:
                        ans.append(v)
                if len(ans) > 0 and ans[0] == 0:
                    return '0'
                else:
                    return ''.join([str(v) for v in ans])

        return ''
    
digits = [1]
# digits = [8,6,7,1,0]
# digits = [1,2,0,0,0]
digits = [9,8,6,8,6]

sol = Solution()
print(sol.largestMultipleOfThree(digits))
