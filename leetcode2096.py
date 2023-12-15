
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
    #TLE 数组拷贝的耗时
    def getDirections2(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        #0 start, 1 end, -1 nothing, 2 lca
        # 返回PATH
        @cache
        def dfs(root: Optional[TreeNode], startValue: int):
            if root == None:
                return []
            elif root.val == startValue:
                return [root]
            left = dfs(root.left, startValue)
            right = dfs(root.right, startValue)
            if len(left) > 0:
                return [root] + left
            elif len(right) > 0:
                return [root] + right
            else:
                return []
            return
        spath = dfs(root, startValue)
        dpath = dfs(root, destValue)
        cnt = min(len(spath), len(dpath))
        lca = None
        ans = []
        for i in range(cnt + 1):
            if i ==cnt or spath[i].val != dpath[i].val:
                ans += ["U"] * (len(spath) - i)
                for j in range(i, len(dpath)):
                    if lca.left == dpath[j]:
                        ans.append("L")
                    elif lca.right == dpath[j]:
                        ans.append("R")
                    lca = dpath[j]
                break
            lca = spath[i]

        return ''.join(ans)
    
    #TLE 可能问题出在数组拷贝上
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        #0 start, 1 end, -1 nothing, 2 lca
        # 返回PATH
        def dfs(root: Optional[TreeNode], startValue: int, path: List):
            if root == None:
                return False
            elif root.val == startValue:
                return True
            
            left = dfs(root.left, startValue, path)
            if left:
                path.append(root.left)
                return True
            
            right = dfs(root.right, startValue, path)
            if right:
                path.append(root.right)
                return True
            else:
                return False
            return
        spath = []
        dfs(root, startValue, spath)
        spath.append(root)
        spath = spath[::-1]
        dpath = []
        dfs(root, destValue, dpath)
        dpath.append(root)
        dpath = dpath[::-1]
        cnt = min(len(spath), len(dpath))
        lca = None
        ans = []
        for i in range(cnt + 1):
            if i ==cnt or spath[i].val != dpath[i].val:
                ans += ["U"] * (len(spath) - i)
                for j in range(i, len(dpath)):
                    if lca.left == dpath[j]:
                        ans.append("L")
                    elif lca.right == dpath[j]:
                        ans.append("R")
                    lca = dpath[j]
                break
            lca = spath[i]

        return ''.join(ans)
            

    
root = TreeNode(5)
root.left = TreeNode(1, TreeNode(3))
root.right = TreeNode(2, TreeNode(6), TreeNode(4))
sol = Solution()
print(sol.getDirections(root,3,6))
