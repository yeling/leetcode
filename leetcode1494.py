
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

class Solution:
    # 56 / 81
    # BFS 是错误的，有些可能先学较好，需要状态压缩DP
    def minNumberOfSemesters2(self, n: int, relations: List[List[int]], k: int) -> int:
        inDegree = [0] * (n + 1)
        outList = [[] for _ in range(n + 1)]
        for x,y in relations:
            inDegree[y] += 1
            outList[x].append(y)
        #(inDegree, index)
        stack = []
        ans = 0
        for i in range(1,n+1):
            if inDegree[i] == 0:
                stack.append(i)
        while len(stack) > 0:
            i = 0
            cnt = len(stack)
            while i < k and i < cnt:
                temp = stack.pop()
                # print(temp)
                for v in outList[temp]:
                    inDegree[v] -= 1
                    if inDegree[v] == 0:
                        stack.append(v)
                i += 1
            ans += 1
        
        return ans
    

    # BFS 是错误的，有些可能先学较好，需要状态压缩DP
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        inDegree = [0] * (n + 1)
        outList = [[] for _ in range(n + 1)]
        for x,y in relations:
            inDegree[y] += 1
            outList[x].append(y)
        #(inDegree, index)
        stack = []
        ans = 0
        for i in range(1,n+1):
            if inDegree[i] == 0:
                stack.append(i)
        while len(stack) > 0:
            i = 0
            cnt = len(stack)
            while i < k and i < cnt:
                temp = stack.pop()
                # print(temp)
                for v in outList[temp]:
                    inDegree[v] -= 1
                    if inDegree[v] == 0:
                        stack.append(v)
                i += 1
            ans += 1
        
        return ans
    
n = 4
relations = [[2,1],[3,1],[1,4]]
k = 3
n = 5
relations = [[2,1],[3,5],[4,1],[1,5]]
k = 2

n = 11
relations = []
k = 2

n = 13
relations = [[12,8],[2,4],[3,7],[6,8],[11,8],[9,4],[9,7],[12,4],[11,4],[6,4],[1,4],[10,7],[10,4],[1,7],[1,8],[2,7],[8,4],[10,8],[12,7],[5,4],[3,4],[11,7],[7,4],[13,4],[9,8],[13,8]]
k = 9

sol = Solution()
print(sol.minNumberOfSemesters(n, relations, k))
