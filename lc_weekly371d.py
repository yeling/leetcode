
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
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        return
    
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:  
        nums.sort()
        root = Node()
        for v in nums:
            temp = [int(i) for i in bin(v)[2:]]
            last = [0] * (20 - len(temp)) + temp  
            curr = root
            for i in last:
                if i == 0:
                    if curr.left == None:
                        curr.left = Node()
                    curr = curr.left
                elif i == 1:
                    if curr.right == None:
                        curr.right = Node()
                    curr = curr.right
        ans = 0
        for v in nums:
            temp = [int(i) for i in bin(v)[2:]]
            last = [0] * (20 - len(temp)) + temp
            start = 20 - len(temp) - 1
            i = 0
            curr = root
            while i < start and curr.left != None:
                curr = curr.left
                i += 1
            if i == start:
                value = 0
                while i <= 20:
                    if last[i] == 0:
                        if curr.right != None:
                            curr = curr.right
                        elif curr.left != None:
                            curr = curr.left
                        
                        

            






        return
    
nums = [1,2,3,4,5]
n2 = [2,3]
print(nums + n2)
sol = Solution()
print(sol.maximumStrongPairXor(nums))
