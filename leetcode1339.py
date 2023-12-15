
# auther yeling
from typing import * 
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 32 / 54 
    # 763478770 998864274
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 10 ** 9 + 7
        def dfs(node):
            sum = node.val
            if node.left != None:
                sum += dfs(node.left)
            if node.right != None:
                sum += dfs(node.right)
            return sum%mod

        allSum = dfs(root)
        print(allSum)
        
        global maxRet
        maxRet = 0
        def dfs2(node):
            sum = node.val
            global maxRet
            if node.left != None:
                temp = dfs2(node.left)
                sum += temp
                # print(sum, temp, maxRet, temp * (allSum - temp)%mod)
                maxRet = max(maxRet, temp * (mod + allSum - temp))
            if node.right != None:
                temp = dfs2(node.right)
                sum += temp
                maxRet = max(maxRet, temp * (mod + allSum - temp))
            return sum
        dfs2(root)

        return maxRet%mod

sol = Solution()

a = 10

a = max(a, 20)
print(a)

print()
