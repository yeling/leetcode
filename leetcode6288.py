
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

class DataStream:
    def __init__(self, value: int, k: int):
        self.nums = []
        self.k = k
        self.s = 0
        self.value = value
        return

    def consec(self, num: int) -> bool:
        self.nums.append(num)
        if num != self.value:
            self.s = len(self.nums)
            
        if len(self.nums) - self.s < self.k:
            return False
        else:
            return True
            



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)

sol = Solution()
print()
