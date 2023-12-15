
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        stack = list()
        stack.append(root)
        s = []
        while len(stack) > 0:
            cnt = len(stack)
            tempS = 0
            for i in range(cnt):
                curr = stack[i]
                tempS += curr.val
                if curr.left != None:
                    stack.append(curr.left)
                if curr.right != None:
                    stack.append(curr.right)
            stack = stack[cnt:]
            s.append(tempS)
        s.sort(reverse=True)
        if len(s) < k:
            return -1
        else:
            return s[k-1]
                

    
      
    

sol = Solution()
print()
