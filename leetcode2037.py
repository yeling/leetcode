
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        ans = 0
        for i,j in zip(seats, students):
            ans += abs(i-j)
        return ans
    
seats = [4,1,5,9]
students = [1,3,2,6]
sol = Solution()
print(sol.minMovesToSeat(seats, students))
