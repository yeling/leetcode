
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
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # 层序遍历 None 加进去，第一层是第二层的两倍
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        ans = []
        stack = [root]
        while len(stack) > 0:
            cnt = len(stack)
            for i in range(cnt):
                if stack[i] != None:
                    ans.append(stack[i].val)
                    stack.append(stack[i].left)
                    stack.append(stack[i].right)
                else:
                    ans.append('-1')
            stack = stack[cnt:]
        
        return ",".join([str(v) for v in ans])
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        array = data.split(',')
        n = len(array)
        ans = [TreeNode(int(v)) for v in array]
        i = 0
        j = 1
        print(array)
        while j < n:
            # print(i, j, array[i], n)
            while array[i] == '-1':
                i += 1
            if ans[j].val != -1:
                ans[i].left = ans[j]
            j += 1
            if ans[j].val != -1:
                ans[i].right = ans[j]
            j += 1
            i += 1
            # print(i, j)
        if ans[0].val == -1:
            return None
        return ans[0]

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans    
        
    

# sol = Solution()
# print()
