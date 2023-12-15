
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
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        first = head
        second = head.next
        while second != None:
            temp = ListNode(gcd(first.val, second.val))
            first.next = temp
            temp.next = second
            first = second
            second = second.next
            

        return head
    

sol = Solution()
print()
