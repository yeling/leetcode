
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
    class Allocator:
    def __init__(self, n: int):
        self.n = n
        self.stack = [0] * n
        return

    def allocate(self, size: int, mID: int) -> int:
        # print('allocate' , size, mID)
        left = 0
        right = 0
        while right < self.n:
            # print(left, right)
            if self.stack[right] == 0:
                right += 1
                if right - left == size:
                    for j in range(left,right):
                        self.stack[j] = mID
                        # print(self.stack)
                    return left
            else:
                right = right + 1
                left = right
        # print(self.stack)
        return -1
            
    def free(self, mID: int) -> int:
        s = 0
        for i in range(self.n):
            if self.stack[i] == mID:
                s += 1
                self.stack[i] = 0
        print(self.stack)
        return s


sol = Solution()
print()
