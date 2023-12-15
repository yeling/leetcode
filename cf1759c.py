# auther yeling
from typing import List
import math

class Solution:
    def begin(self, l, r, x, a, b) :
        print(l, r, x, a, b)
        
        return 0

sol = Solution()


caseNum = int(input())
for i in range(0, caseNum):
    first = [int(v) for v in (input()).split(' ')]
    second = [int(v) for v in (input()).split(' ')]
    sol.begin(first[0],first[1],first[2], second[0], second[1])
   
