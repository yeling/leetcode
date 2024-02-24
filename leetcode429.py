
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


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []
        stack = [root]
        ans = []
        while len(stack) > 0:
            sn = len(stack)
            temp = []
            for i in range(sn):
                temp.append(stack[i].val)
                for v in stack[i].children:
                    stack.append(v)
            stack = stack[sn:]
            ans.append(temp)

        return ans
    

sol = Solution()
print()
