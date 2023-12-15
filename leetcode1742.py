
# auther yeling
from typing import List
from bisect import *
from collections import *

MOD = 10 ** 9 + 7

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        cache = defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            s = sum(int(v) for v in str(i))
            cache[s] += 1

        m = 0
        for key in cache:
            m = max(m, cache[key])
        return m

lowLimit = 1
highLimit = 10
lowLimit = 5
highLimit = 15
sol = Solution()
print(sol.countBalls(lowLimit, highLimit))
