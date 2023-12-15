
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

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:   
        stack = []
        while head != None:
            stack.append(head)
            head = head.next
        ans = ListNode()
        curr = None
        flag = 0
        while len(stack) > 0:
            temp = stack.pop()
            curr = (temp.val * 2 + flag)%10
            flag = (temp.val * 2 + flag)//10
            currNode = ListNode(curr, ans.next)
            ans.next = currNode
        if flag != 0:
            currNode = ListNode(flag, ans.next)
            ans.next = currNode
        return ans.next
    

sol = Solution()
print()
