
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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        global ans 
        ans = 0
        #[min,max]
        def dfs(curr, ma):
            ans = max(ans, abs(ma[0] - curr.val), abs(ma[1] - curr.val))
            next = [0,0]
            next[0] = min(ma[0], curr.val)
            next[1] = max(ma[1], curr.val)

            if curr.left != None:
                dfs(curr.left, next)
            if curr.right != None:
                dfs(curr.right, next)
        return ans

sol = Solution()
print()
