
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

#    Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        stack.append(root)
        root.val = 0
        while len(stack)> 0:
            count = len(stack)
            cache = []
            for i in range(count):
                curr = stack[i]
                if curr.left != None:
                    stack.append(curr.left)
                    cache.append(curr.left.val)
                else:
                    stack.append(None)
                    cache.append(0)
                
                if curr.right != None:
                    stack.append(curr.right)
                    cache.append(curr.right.val)
                else:
                    stack.append(None)
                    cache.append(0)
            all = sum(cache)
            next = []
            # print(all, cache)
            for i in range(count, len(stack)):
                if stack[i] != None:
                    next.append(stack[i])
                    # print(stack[i].val, count - i)
                    if (i - count)%2 == 0:
                        stack[i].val = all - cache[i - count] - cache[i - count + 1]
                    else:
                        stack[i].val = all - cache[i - count - 1] - cache[i - count]
            stack = next

        return root
    