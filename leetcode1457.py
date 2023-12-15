
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
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        cnt = [0] * 10
        ans = 0
        def dfs(curr):
            nonlocal ans
            if curr.left == None and curr.right == None:
                odd = 0
                for i in range(1,10):
                    if cnt[i]%2 == 1:
                        odd += 1
                if odd == 0 or odd == 1:
                    ans += 1
                return 

            if curr.left != None:
                cnt[curr.left.val] += 1
                dfs(curr.left)
                cnt[curr.left.val] -= 1

            if curr.right != None:
                cnt[curr.right.val] += 1
                dfs(curr.right)
                cnt[curr.right.val] -= 1
                
            return 
        
        cnt[root.val] += 1
        dfs(root)

        return ans
    

sol = Solution()
print()
