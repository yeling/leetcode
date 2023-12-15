
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
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:    
        self.ans = []
        cache = set(to_delete)
        def dfs(curr, remove):
            if curr.left != None:
                dfs(curr.left, curr.left.val in cache)
                if remove:
                    if curr.left.val not in cache:
                        self.ans.append(curr.left)
                    curr.left = None
                elif curr.left.val in cache:
                    curr.left = None

                
            if curr.right != None:
                dfs(curr.right, curr.right.val in cache)
                if remove:
                    if curr.right.val not in cache:
                        self.ans.append(curr.right)
                    curr.right = None
                elif curr.right.val in cache:
                    curr.right = None
            return 
        
        if root.val not in cache:
            self.ans.append(root)
        dfs(root, root.val in cache)
        
        return self.ans
    

sol = Solution()
print()
