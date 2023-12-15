
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
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    #树形DP，后序遍历， @cache 
    def minCameraCover2(self, root: Optional[TreeNode]) -> int:
        #[not have, have]
        @cache
        def dfs(u, faFlag):
            if u == None :
                return [0,INF]
            if u.left == None and u.right == None:
                if faFlag:
                    return [0,1]
                else:
                    return [INF,1]
            
            have = 0
            notHave = 0
            if faFlag:
                l = dfs(u.left, True)
                r = dfs(u.right, True)
                have = 1 + min(l[0] + r[0], l[1] + r[0], l[0] + r[1], l[1] + r[1])

                l = dfs(u.left, False)
                r = dfs(u.right, False)
                notHave = min(l[0] + r[0], l[1] + r[0], l[0] + r[1], l[1] + r[1])
            else:
                l = dfs(u.left, True)
                r = dfs(u.right, True)
                have = 1 + min(l[0] + r[0], l[1] + r[0], l[0] + r[1], l[1] + r[1])

                l = dfs(u.left, False)
                r = dfs(u.right, False)
                notHave = min( l[1] + r[0], l[0] + r[1], l[1] + r[1])
            # print(faFlag,u, [notHave, have] )
            return [notHave, have]

        ans = dfs(root, False)

        return min(ans[0], ans[1])
    

    #树形DP，后序遍历， @cache 
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        #ans[i][j] i 表示 faFlag false,true,j 表示自己 not have, have
        @cache
        def dfs(u):
            if u == None :
                return [[0,INF],[0,INF]]
            if u.left == None and u.right == None:
                return [[INF,1],[0,1]]
            
            l = dfs(u.left)
            r = dfs(u.right)
            ans = [[INF,INF],[INF,INF]]
            ans[0][0] = min( l[0][1] + r[0][0], l[0][0] + r[0][1], l[0][1] + r[0][1])
            ans[0][1] = 1 + min(l[1][0], l[1][1]) + min(r[1][0], r[1][1]) 
            ans[1][0] = min(l[0][0], l[0][1]) + min(r[0][0], r[0][1])
            ans[1][1] = 1 + min(l[1][0], l[1][1]) + min(r[1][0], r[1][1]) 
            
            return ans

        ans = dfs(root)

        return min(ans[0][0], ans[0][1])
    
# sol = Solution()
# print()
