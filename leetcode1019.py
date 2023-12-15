
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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        #(value, pos)
        stack = []
        temp = head
        i = 0
        while temp != None:
            ans.append(0)
            if len(stack) == 0 or stack[-1][0] >= temp.val:
                stack.append((temp.val,i))
            else:
                while len(stack) > 0 and stack[-1][0] < temp.val:
                    ans[stack[-1][1]] = temp.val
                    stack.pop()
                stack.append((temp.val,i))
            temp = temp.next
            i += 1

        return ans
    

sol = Solution()
print()
