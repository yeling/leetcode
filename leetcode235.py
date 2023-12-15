
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
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        vis = defaultdict(bool)
        vis2 = defaultdict(bool)
        ans = None
        def dfs(curr: TreeNode, dst: TreeNode):
            nonlocal vis, ans
            if curr == None:
                return False
            if curr.val == dst.val:
                vis[curr] = True          
            else:
                vis[curr] = dfs(curr.left, dst) or dfs(curr.right, dst)
            return vis[curr]
        
        def dfs2(curr: TreeNode, dst: TreeNode):
            nonlocal vis, vis2, ans
            if curr == None:
                return False
            if curr.val == dst.val:
                vis2[curr] = True   
            else:
                vis2[curr] = dfs2(curr.left, dst) or dfs2(curr.right, dst)
            if vis2[curr] == True and vis[curr] == True and ans == None:
                ans = curr
            return vis2[curr]

        dfs(root, p)
        dfs2(root, q)
        return ans
   