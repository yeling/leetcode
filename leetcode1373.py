
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
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        #(flag, value, min, max)
        def dfs(temp):
            l = [True, INF, INF, -INF]
            if temp.left != None:
                l = dfs(temp.left)
            r = [True, INF, INF, -INF]
            if temp.right != None:
                r = dfs(temp.right)
            ret = [False, temp.val, temp.val, temp.val]
            if l[0] and r[0] and l[3] < temp.val and temp.val < r[2]:
                ret[0] = True
                if temp.left != None:
                    ret[1] += l[1]
                if temp.right != None:
                    ret[1] += r[1]
                self.ans = max(self.ans, ret[1])
                ret[2] = min(ret[2], l[2], r[2])
                ret[3] = max(ret[3], r[3], r[3])

            return ret
        dfs(root)
        return self.ans
    
