
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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int: 
        self.ans = 0
        def dfs(curr:TreeNode, ma: int):
            if curr.val >= ma:
                self.ans += 1
            if curr.left != None:
                dfs(curr.left, max(curr.val, ma))
            if curr.right != None:
                dfs(curr.right, max(curr.val, ma))
            return
        dfs(root, -INF)
        return self.ans
    

sol = Solution()
print()
