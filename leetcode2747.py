
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

class Node:
    def __init__(self):
        self.val = set()
        self.add = 0
        self.left = None
        self.right = None
        return

class SegmentTreeDynamic:
    def __init__(self):
        self.N = 10 ** 9
        # self.N = 20
        self.root = Node()

    def update(self,  node, start, end, l, r, val):
        if l <= start and end <= r:
            node.val.add(val)
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
        ans = set()
        self.pushDown(node, mid - start + 1, end - mid)
        if l <= mid: ans |= self.query(node.left, start, mid, l, r)
        if r > mid: ans |= self.query(node.right, mid + 1, end, l, r)
        return ans
        
    def pushUp(self, node):
        node.val = node.left.val | node.right.val
        return
    
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
    

class Solution:
    #MLE
    #TLE
    # 2123 / 3129 个通过测试用例
    def countServers2(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:    
        
        tree = SegmentTreeDynamic()

        for s,t in logs:
            tree.update(tree.root, 0, tree.N, t, t, s)
        
        ans = []
        for v in queries:
            l = v - x
            r = v
            ret = tree.query(tree.root, 0, tree.N, l, r)
            # print(ret)
            ans.append(n - len(ret))

        return ans
    
    #滑动窗口
    def countServers2(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:    
        cache = defaultdict(list)
        for id,time in logs:
            cache[time].append(id)
        tn = max(max(queries), max(list(cache.keys()))) + 1
        # tn = 20
        l,r = 0, 0
        curr = defaultdict(int)
        alltime = [0] * tn
        while r < tn:
            # print(r, alltime)
            for v in cache[r]:
                curr[v] += 1
            if r - l == x + 1:
                for v in cache[l]:
                    curr[v] -= 1
                    if curr[v] == 0:
                        del curr[v]
                l += 1
            alltime[r] = n - len(curr)
            r += 1
            
        ans = []
        for q in queries:
            ans.append(alltime[q])

        return ans
    
    # 滑动窗口
    # 时间卡的比较厉害
    # 2153 / 3129 
    # AC 滑动窗口，在两个数组间滑动
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:    
       
        logs.sort(key=lambda x:x[1])
        curr = defaultdict(int)
        qs = list(zip(range(len(queries)), queries))
        qs.sort(key = lambda x:x[1])
        # print(qs)
        l,r = 0, 0
        ans = [0] * len(qs)
        temp = 0
        for q in qs:
            # r 进入区间
            while r < len(logs) and logs[r][1] <= q[1]:
                if curr[logs[r][0]] == 0:
                    temp += 1
                curr[logs[r][0]] += 1
                r += 1
            # l 退出区间
            while  l < len(logs) and logs[l][1] < q[1] - x:
                curr[logs[l][0]] -= 1
                if curr[logs[l][0]] == 0:
                    temp -= 1
                l += 1
            ans[q[0]] = n - temp

        return ans
    

n = 3
logs = [[1,3],[2,6],[1,5]]
x = 5
queries = [10,11]

n = 3
logs = [[2,4],[2,1],[1,2],[3,1]]
x = 2
queries = [3,4]

# n = 4
logs = [[1,10],[3,15],[3,19],[1,13],[2,24],[1,3],[2,26]]
x = 2
queries = [22,16,18,5,27]
# n = 3
# logs = [[2,4],[2,1],[1,2],[3,1]]
# x = 2
# queries = [3,4]
sol = Solution()
print(sol.countServers2(n, logs, x, queries))
print(sol.countServers(n, logs, x, queries))
