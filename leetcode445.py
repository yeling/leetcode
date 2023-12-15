
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  
        v1 = ''
        while l1 != None:
            v1 += str(l1.val)
            l1 = l1.next
        
        v2 = ''
        while l2 != None:
            v2 += str(l2.val)
            l2 = l2.next
        
        print(v1, v2)

        res = str(int(v1) + int(v2))
        ans = ListNode(int(res[0]))
        curr = ans
        for i in range(1, len(res)):
            curr.next = ListNode(int(res[i]))
            curr = curr.next
        return ans
    

sol = Solution()
print()
