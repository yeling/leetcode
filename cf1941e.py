# auther yeling
import sys
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from heapq import *
import string
from os import path
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"


# for I/O for local system
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    # sys.stdout = open("output.txt","w")

# For fast I/O
# input = sys.stdin.buffer.readline
input = sys.stdin.readline
# print = sys.stdout.write

"""
The "sorted list" data-structure, with amortized O(n^(1/3)) cost per insert and pop.

Example:

A = SortedList()
A.insert(30)
A.insert(50)
A.insert(20)
A.insert(30)
A.insert(30)

print(A) # prints [20, 30, 30, 30, 50]

print(A.lower_bound(30), A.upper_bound(30)) # prints 1 4

print(A[-1]) # prints 50
print(A.pop(1)) # prints 30

print(A) # prints [20, 30, 30, 50]
print(A.count(30)) # prints 2

"""

from bisect import bisect_left as lower_bound
from bisect import bisect_right as upper_bound


class FenwickTree:
    def __init__(self, x):
        bit = self.bit = list(x)
        size = self.size = len(bit)
        for i in range(size):
            j = i | (i + 1)
            if j < size:
                bit[j] += bit[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < self.size:
            self.bit[idx] += x
            idx |= idx + 1

    def __call__(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def find_kth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(self.size.bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < self.size and self.bit[right_idx] <= k:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1, k


class SortedList:
    block_size = 10000

    def __init__(self, iterable=()):
        self.macro = []
        self.micros = [[]]
        self.micro_size = [0]
        self.fenwick = FenwickTree([0])
        self.size = 0
        for item in iterable:
            self.insert(item)

    def insert(self, x):
        i = lower_bound(self.macro, x)
        j = upper_bound(self.micros[i], x)
        self.micros[i].insert(j, x)
        self.size += 1
        self.micro_size[i] += 1
        self.fenwick.update(i, 1)
        if len(self.micros[i]) >= self.block_size:
            self.micros[i:i + 1] = self.micros[i][:self.block_size >> 1], self.micros[i][self.block_size >> 1:]
            self.micro_size[i:i + 1] = self.block_size >> 1, self.block_size >> 1
            self.fenwick = FenwickTree(self.micro_size)
            self.macro.insert(i, self.micros[i + 1][0])

    def pop(self, k=-1):
        i, j = self._find_kth(k)
        self.size -= 1
        self.micro_size[i] -= 1
        self.fenwick.update(i, -1)
        return self.micros[i].pop(j)

    def __getitem__(self, k):
        i, j = self._find_kth(k)
        # print(i,j)
        return self.micros[i][j]

    def count(self, x):
        return self.upper_bound(x) - self.lower_bound(x)

    def __contains__(self, x):
        return self.count(x) > 0

    def lower_bound(self, x):
        i = lower_bound(self.macro, x)
        return self.fenwick(i) + lower_bound(self.micros[i], x)

    def upper_bound(self, x):
        i = upper_bound(self.macro, x)
        return self.fenwick(i) + upper_bound(self.micros[i], x)

    def _find_kth(self, k):
        return self.fenwick.find_kth(k + self.size if k < 0 else k)

    def __len__(self):
        return self.size

    def __iter__(self):
        return (x for micro in self.micros for x in micro)

    def __repr__(self):
        return str(list(self))
    
input = lambda: sys.stdin.readline().rstrip()
si = lambda :int(input())
mi = lambda :map(int,input().split())
li = lambda :list(mi())

def solve2(n, m, k, d, grid):
    row = [0] * n
    
    for i in range(n):
        cache = [INF] * m
        temp = SortedList()
        cache[0] = 1
        temp.insert((1,0))
        for j in range(1,m):
            while j - temp[0][1] > d + 1:
                temp.pop(0)
                # print(i, j, row, temp)
            cache[j] = temp[0][0] + grid[i][j] + 1
            temp.insert((cache[j], j))
            # print(i, j, cache, temp)
        row[i] = cache[m - 1]
    ans = INF
    curr = 0
    for i in range(n):
        curr += row[i]
        if i + 1>= k:
            if i - k >= 0:
                curr -= row[i - k]
            ans = min(ans, curr)
        
    print(ans)

    return 

def solve(n, m, k, d, grid):
    row = [0] * n
    
    for i in range(n):
        cache = [INF] * m
        temp = SortedList()
        cache[0] = 1
        temp.insert((1,0))
        for j in range(1,m):
            while j - temp[0][1] > d + 1:
                temp.pop(0)
                # print(i, j, row, temp)
            cache[j] = temp[0][0] + grid[i][j] + 1
            temp.insert((cache[j], j))
            # print(i, j, cache, temp)
        row[i] = cache[m - 1]
    ans = INF
    curr = 0
    for i in range(n):
        curr += row[i]
        if i + 1>= k:
            if i - k >= 0:
                curr -= row[i - k]
            ans = min(ans, curr)
        
    print(ans)

    return 


caseNum = int(input())
for i in range(0, caseNum):
    n,m,k,d = li()
    grid = []
    for _ in range(n):
        grid.append(li())
    solve(n, m, k, d, grid)

   