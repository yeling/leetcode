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
# input = sys.stdin.readline
# print = sys.stdout.write

input = lambda: sys.stdin.readline().rstrip()
si = lambda :int(input())
mi = lambda :map(int,input().split())
li = lambda :list(mi())

class Node:
    def __init__(self):
        self.val = 0
        self.add = 0
        self.left = None
        self.right = None
        return

class SegmentTreeDynamic:
    def __init__(self, n):
        self.N = n
        self.root = Node()

    def update(self,  node, start, end, l, r, val):
        if l <= start and end <= r:
            # 对区间进行「加减」的更新操作，需要 +=
            node.val += (end - start + 1) * val
            node.add += val
            return 
        
        mid = (start + end) >> 1
        self.pushDown(node, mid - start + 1, end - mid)
        if l <= mid: self.update(node.left, start, mid, l, r, val)
        if r > mid: self.update(node.right, mid + 1, end, l, r, val)
        self.pushUp(node)
    

    def query(self, node, start, end, l, r):
        if l <= start and end <= r:
            return node.val
        mid = (start + end) >> 1
        #注意区间和的表示方法
        ans = 0
        self.pushDown(node, mid - start + 1, end - mid)
        if l <= mid: ans += self.query(node.left, start, mid, l, r)
        if r > mid: ans += self.query(node.right, mid + 1, end, l, r)
        return ans
        
    def pushUp(self, node):
        #注意区间和的上推
        node.val = node.left.val + node.right.val
    
    def pushDown(self, node, leftNum, rightNum):
        if node.left == None: node.left = Node()
        if node.right == None: node.right = Node()
        if node.add == 0: return 
        
        node.left.val += node.add
        node.right.val += node.add
        # # 对区间进行「加减」的更新操作，下推懒惰标记时需要累加起来，不能直接覆盖
        node.left.add += node.add
        node.right.add += node.add
        node.add = 0

def solve2(n, nums):
    # print(n, nums)
    cache = [((i + 1 + v), -i) for i,v in enumerate(nums)]
    cache.sort(reverse=True)
    print(cache)
    ans = []
    tree = SegmentTreeDynamic(n)
    for v,i in cache:
        pos = -i
        temp = tree.query(tree.root, 0, tree.N, 0, pos)
        ans.append(v - temp)
        tree.update(tree.root, 0, tree.N, pos, n, 1)

    print(*ans)


    return 

def solve(n, nums):
    # print(n, nums)
    cache = [((i + 1 + v), -i) for i,v in enumerate(nums)]
    cache.sort(reverse=True)
    ct = Counter([i + 1 + v for i,v in enumerate(nums)])
    print(cache)
    ans = set()
    
    for i in range(n-1, -1, -1):
        if ct[nums[i] + i + 1] == 1:
            ans.add(nums[i] + i + 1)
        else:

        


    print(*ans)


    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)

   
