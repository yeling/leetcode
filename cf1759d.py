# auther yeling
from typing import List
import math

class Solution:
    def begin(self, n: int, m: int) :
        print('begin ', n, m)
        two = 0
        temp = n
        while temp & 1 == 0:
            temp >>= 1
            two += 1
        five = 0
        temp = n
        while temp%5 == 0:
            temp /= 5
            five += 1
        print(two, five)

        twom = 0
        temp = m
        while temp >= 2:
            temp //= 2
            twom += 1
        fivem = 0
        temp = m
        while temp >= 5:
            temp //= 5
            fivem += 1
        print(twom, fivem)



        return 0

sol = Solution()


caseNum = int(input())
for i in range(0, caseNum):
    first = [int(v) for v in (input()).split(' ')]
    sol.begin(first[0], first[1])
   
