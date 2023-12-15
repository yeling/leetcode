
# auther yeling
from typing import List
from bisect import *
from collections import *

MOD = 10 ** 9 + 7

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        curr = 0
        for v in gain:
            curr += v
            res = max(res, curr)
        return res


gain = [-5,1,5,0,-7]
gain = [-4,-3,-2,-1,4,3,2]
sol = Solution()
print(sol.largestAltitude(gain))
