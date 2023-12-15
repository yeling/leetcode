
# auther yeling
from typing import List
from bisect import *
from collections import *

MOD = 10 ** 9 + 7


class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        n = len(s)
        prime = [2,3,5,7]
        if s[0] not in prime or s[-1] in prime:
            return 0
        if k * minLength > n:
            return 0
        
        
    
        dp = [[0] * (k + 1) for _ in range(n)]
        for bi in range(n-1, -1, -1):
            
            print(bi)

        print(dp)

        return


s = "23542185131"
k = 3
minLength = 2
sol = Solution()
print(sol.beautifulPartitions(s, k, minLength))
