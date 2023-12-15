
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
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        cache = [temp]
        while temp.next != None:
            cache.append(temp.next)
            temp = temp.next
        l = 0
        r = len(cache) - 1
        while l < r:
            cache[l].next = cache[r]
            if l + 1 < r:
                cache[r].next = cache[l + 1]
            l += 1
            r -= 1

        return
    

sol = Solution()
print()
