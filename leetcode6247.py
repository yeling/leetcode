
# auther yeling
from typing import *
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue


MOD = 10 ** 9 + 7

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = Deque()
        temp = head
        while temp != None:
            while len(stack) > 0:
                curr = stack[len(stack) - 1]
                if curr.val < temp.val:
                    stack.pop()
                else:
                    break
            stack.append(temp)
            temp = temp.next
        
        res = stack[0]
        for i in range(len(stack) - 1):
            stack[i].next = stack[i+1]
        return res


# [5,2,13,3,8]
head = ListNode(1,None)
head.next = ListNode(1,None)
head.next.next = ListNode(1,None)
head.next.next.next = ListNode(1,None)
head.next.next.next.next = ListNode(1,None)
sol = Solution()
re = sol.removeNodes(head)
while re != None:
    print(re.val)
    re = re.next

