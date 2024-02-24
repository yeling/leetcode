
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        ans = []
        stack = [root]
        flag = True
        while len(stack) > 0:
            sn = len(stack)
            temp = []
            for i in range(sn):
                temp.append(stack[i].val)
                if stack[i].left != None:
                    stack.append(stack[i].left)

                if stack[i].right != None:
                    stack.append(stack[i].right)
            stack = stack[sn:]
            if flag:
                ans.append(temp[:])
            else:
                ans.append(temp[::-1])
            flag = not flag

        return ans
    

sol = Solution()
print()
