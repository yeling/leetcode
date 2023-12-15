
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
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class TreeAncestor:
    # 14 / 17 个通过的测试用例
    # 16 / 17 个通过的测试用例
    def __init__(self, n: int, parent: List[int]):
        ma = int(log(n,2)) + 1
        #value, pos
        self.n = n
        self.dp = [[p] + [-1]*ma for p in parent]
        # print(self.dp)
        for j in range(ma):
            for i in range(n):
                pa = self.dp[i][j]
                if pa != -1:
                    self.dp[i][j + 1] = self.dp[pa][j]
                else:
                    # print(i, j)
                    self.dp[i][j + 1] = -1
            # print(self.dp)
        return


    def getKthAncestor(self, node: int, k: int) -> int:
        pa = node
        for i in range(len(bin(k)) - 2):
            if (1 << i & k) != 0:
                pa = self.dp[pa][i]
                if pa == -1:
                    return -1
        # print(pa)
        return pa



# Your TreeAncestor object will be instantiated and called as such:
# treeAncestor = TreeAncestor(7, [-1, 0, 1, 2, 3, 4, 5])
# print(treeAncestor.getKthAncestor(3, 5)); 
# param_1 = obj.getKthAncestor(node,k)   
 
# [[6,[-1,2,3,4,5,0]],[1,4]]
treeAncestor = TreeAncestor(6, [-1,2,3,4,5,0])
print(treeAncestor.getKthAncestor(1, 4)); 

    
