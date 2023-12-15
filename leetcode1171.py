
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
    def removeZeroSumSublists2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cache = defaultdict(ListNode)
        dummyHead = ListNode()
        dummyHead.next = head
        cache[0] = dummyHead
        preSum = 0
        i = 0
        temp = head
        while temp != None:
            preSum += temp.val
            if preSum in cache:
                cache[preSum].next = temp.next
                # cache[preSum] = temp
            else:
                cache[preSum] = temp
            temp = temp.next
            # print(i, preSum)
        
        return dummyHead.next

    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head
        #(node, preSum)
        cache = [(dummyHead, 0)]
        preSum = 0
        temp = head
        while temp != None:
            preSum += temp.val
            flag = False
            cnt = len(cache)
            for i in range(cnt):
                if cache[i][1] == preSum:
                    flag = True
                    cache[i][0].next = temp.next
                    cache = cache[0:i+1]
                    break
            if flag == False:
                cache.append((temp,preSum))
            temp = temp.next
            # print(i, cache)
        return dummyHead.next
    

sol = Solution()
head = ListNode(0)
head.next = ListNode(1)
head.next.next  = ListNode(1)
print(sol.removeZeroSumSublists(head))
