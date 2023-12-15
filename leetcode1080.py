
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
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
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:    
        def dfs(root , p, value):
            #叶子结点
            if root.left == None and root.right == None:
                if value + root.val >= limit:
                    return True
                else: 
                    return False
                
            l, r = False, False
            if root.left != None:
                l = dfs(root.left, root, value + root.val)
                if l == False:
                    root.left = None
            if root.right != None:
                r = dfs(root.right, root, value + root.val)
                if r == False:
                    root.right = None
            return l or r
        
             
        temp = root
        ret = dfs(root, None, 0)
        if ret == False:
            temp = None
        return temp
    

sol = Solution()
print()