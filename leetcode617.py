
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

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]):
            if node1 == None:
                return node2
            elif node2 == None:
                return node1
            next = TreeNode(node1.val + node2.val)
            next.left = dfs(node1.left, node2.left)
            next.right  = dfs(node1.right, node2.right)
            return next
        
        return dfs(root1, root2)
    

sol = Solution()
print()
