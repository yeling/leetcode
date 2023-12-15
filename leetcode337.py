
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
    def rob2(self, root: Optional[TreeNode]) -> int:  
        @cache  
        def dfs(root: TreeNode, flag: bool):
            if root == None:
                return 0
            if flag == False:
                left =  max(dfs(root.left, True), dfs(root.left, False))
                right = max(dfs(root.right, True), dfs(root.right, False))
                return left + right
            else:
                return dfs(root.left, False) + dfs(root.right, False) + root.val

            return 
        return max(dfs(root, True), dfs(root, False))
    
    def rob(self, root: Optional[TreeNode]) -> int:  
        #[0,0] false,true
        @cache  
        def dfs(root: TreeNode):
            if root == None:
                return [0,0]
            left = dfs(root.left)
            right = dfs(root.right)
            return [max(left) + max(right), root.val + left[0] + right[0]]
        return max(dfs(root))
    

sol = Solution()
print()
