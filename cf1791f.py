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
        # print('update', start, end, l, r, (start + end) >> 1, val)
        if l <= start and end <= r:
            node.val += val
            # node.val += (end - start + 1) * val
            node.add += val
            return 
        
        mid = (start + end) >> 1
        self.pushDown(node, mid - start + 1, end - mid)
        if l <= mid: self.update(node.left, start, mid, l, r, val)
        if r > mid: self.update(node.right, mid + 1, end, l, r, val)
        self.pushUp(node)
    

    def query(self, node, start, end, l, r):
        # print('query', start, end, l, r, (start + end) >> 1, node.val, node.add)
        if l <= start and end <= r:
            return node.val
        mid = (start + end) >> 1
        ans = 0
        self.pushDown(node, mid - start + 1, end - mid)
        if l <= mid: ans = self.query(node.left, start, mid, l, r)
        if r > mid: ans = self.query(node.right, mid + 1, end, l, r)
        return ans
        
    def pushUp(self, node):
        return
        # node.val = min(node.left.val , node.right.val)
    
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

def main(n, q, nums, qs):
    tree = SegmentTreeDynamic(n)
    # print('begin ', tree.N)
    for q in qs:
        # print(q)
        if q[0] == 1:
            tree.update(tree.root, 0, tree.N, q[1] - 1, q[2] - 1, 1)
        elif q[0] == 2:
            ch = tree.query(tree.root, 0, tree.N, q[1] - 1, q[1] - 1)
            temp = nums[q[1] - 1]
            # print(q, ch)
            while ch > 0 and temp > 10:
                next = temp%10
                while temp >= 10:
                    temp //= 10
                    next += temp%10
                temp = next
                ch -= 1
            if temp < 10:
                nums[q[1] - 1] = temp
            print(temp)            
    return 

# n = 5
# q = 3
# nums = [1, 420, 69, 1434, 2023]
# qs = [[1,2,3],[2,2],[2,3],[2,4],[1,2,5],[2,1],[2,3],[2,5]]
# main(n, q, nums, qs)

caseNum = int(input())
for i in range(0, caseNum):
    n,q = li()
    nums = li()
    qs = []
    for j in range(q):
        qs.append(li())
    main(n, q, nums, qs)
    
   
