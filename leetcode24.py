
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        first = head
        second = head.next
        dummy.next = second
        curr = dummy
        while first != None and second != None:
            first.next = second.next
            second.next = first
            curr.next = second

            curr = first
            first = first.next
            if first != None:
                second = first.next
            
        return dummy.next
    

sol = Solution()
print()
