
# auther yeling
from typing import *
from bisect import *
from collections import *

MOD = 10 ** 9 + 7

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        def dfs(root, all):
            if root == None:
                return 
            if root != None:
                all.append(root.val)
            if root.left != None:
                dfs(root.left, all)
            if root.right != None:
                dfs(root.right,all)
            return
        all = []
        dfs(root, all)
        # all = [4,9]
        # queries = [3]
        res = []
        all.sort()
        # print(all)
        for v in queries:
            left = bisect(all, v)
            # print(left)
            temp = [0]*2
            if left == 0:
                temp[0] = -1
                temp[1] = all[0]
                if left == len(all):
                    temp[1] = -1
            elif v == all[left - 1]:
                temp[0] = temp[1] = all[left - 1]
            else:
                temp[0] = all[left - 1]
                if left == len(all):
                    temp[1] = -1
                else :
                    temp[1] = all[left]
            # print(temp)
            # print(all[temp[0]], all[temp[1]])
            res.append(temp)
        return res
            



sol = Solution()
queries = [0,9,16]
print(sol.closestNodes(None, queries))
