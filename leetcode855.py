
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

class Node:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.next = None
        self.parent = None
    def __lt__(self, other):
        if self.r - self.l  == other.r - other.l:
            return self.l < other.l
        else:
            return  self.r - self.l > other.r - other.l
    def __str__(self):
        return '(' + str(self.l)+',\'' + self.r + '\')'

class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.stack = PriorityQueue()
        self.leave = defaultdict(Node)
        return

    def seat(self) -> int:
        if len(self.stack) == 0:
            self.stack.put(Node(0,self.n))
        else:
            top = self.stack.get()
            #最后一个N没被占用
            if top.r == self.n:
                top.l = self.n - 1
                self.stack.put(top)
                add = Node(self.n - 1, self.n - 1)
                add.parent = top
                top.next = add
                self.stack.put(add)
                return add.l
            else:
                add = Node(self.n - 1, self.n - 1)
                top.l = self.n - 1
                self.stack.put(top)
                add.parent = top
                top.next = add
                self.stack.put(add)
                return add.l

        return

    def leave(self, p: int) -> None:
        curr = self.leave[p]
        if curr.parent != None:
            curr.parent.r = curr.r
            curr.parent.next = curr.next
        elif curr.next != None:
            curr.next.l = curr.l
        else:
            self.stack.clear()
            self.leave = defaultdict(Node)
        return


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)  

sol = Solution()
print()
