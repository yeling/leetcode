
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
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:  
        allPath = [[]] * 1001
        # print(allPath)  
        def dfs(curr:TreeNode, path):
            nonlocal allPath
            if curr.left != None:
                dfs(curr.left, path[:] + [curr])
            if curr.right != None:
                dfs(curr.right, path[:] + [curr])
            if curr.left == None and curr.right == None:
                allPath[curr.val] = path[:] + [curr]
        dfs(root, [])
        allPath.sort(key = lambda x: len(x), reverse=True)
        ans = None
        leaf = []
        for v in allPath:
            # print(len(v))
            if len(v) == len(allPath[0]):
                leaf.append(v)
            else:
                break
        flag = False
        for i in range(len(leaf[0])):
            for j in range(len(leaf)):
                if leaf[j][i] == leaf[0][i]:
                    continue
                else:
                    flag = True
                    break
            if flag:
                break
            else:
                ans = leaf[0][i]
        return ans
    

sol = Solution()
print()
