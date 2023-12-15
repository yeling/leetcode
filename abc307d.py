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


# input = lambda: sys.stdin.readline().rstrip()
input = lambda: sys.stdin.readline().rstrip()
sint = lambda :int(input())
mint = lambda :map(int,input().split())
lint = lambda :list(mint())


# Python模版
class Node:
    def __init__(self):
        self.val = 0
        self.add = 0
        self.left = None
        self.right = None
        return

class SegmentTreeDynamic:
    def __init__(self):
        self.N = 10 ** 9
        self.root = Node()

    def update(self,  node, start, end, l, r, val):
        if l <= start and end <= r:
            node.val = val
            # 对区间进行「加减」的更新操作，需要 +=
            # node.val += (end - start + 1) * val
            # node.add += val
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
        ans = INF
        self.pushDown(node, mid - start + 1, end - mid)
        if l <= mid: ans = min(ans, self.query(node.left, start, mid, l, r))
        if r > mid: ans = min(ans, self.query(node.right, mid + 1, end, l, r))
        #注意区间和的表示方法
        # ans = 0
        # self.pushDown(node, mid - start + 1, end - mid)
        # if l <= mid: ans += self.query(node.left, start, mid, l, r)
        # if r > mid: ans += self.query(node.right, mid + 1, end, l, r)
        return ans
        
    def pushUp(self, node):
        node.val = min(node.left.val , node.right.val)
    
    def pushDown(self, node, leftNum, rightNum):
        if node.left == None: node.left = Node()
        if node.right == None: node.right = Node()
        if node.add == 0: return 
        
        # node.left.val += node.add * leftNum
        # node.right.val += node.add * rightNum
        # # 对区间进行「加减」的更新操作，下推懒惰标记时需要累加起来，不能直接覆盖
        # node.left.add += node.add
        # node.right.add += node.add
        # node.add = 0

def solve(n, s):
    #( 的位置 pos
    stack = []
    #删除的位置[l,r]
    ans = []
    for i,v in enumerate(s):
        if v == '(':
            stack.append(i)
        elif v == ')' and len(stack) > 0:
            ans.append([stack.pop(), i])
    print(ans)
    left = []
    for i,v in s:



 
    print(n)



n = int(input())
s = input()
solve(n, s)

