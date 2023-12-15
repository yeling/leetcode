
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

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        ans = [-1] * len(queries)
        #(i,value)
        cache = [list() for _ in range(n)]
        for i,(a,b) in enumerate(queries):
            if a < b and heights[a] < heights[b]:
                ans[i] = b
            elif b < a and heights[b] < heights[a]:
                ans[i] = a
            elif a == b:
                ans[i] = a
            else:
                cache[max(a,b)].append((i,max(heights[a], heights[b]) + 1))
        
        # print(ans, cache)
        #(i, value)
        stack = deque()
        for i in range(n-1, -1, -1):   
            while len(stack) > 0:
                if heights[i] >= stack[0][0]:
                    stack.popleft()
                else:
                    break
            stack.appendleft([heights[i],i])
            for v in cache[i]:
                index = bisect_left(stack, v[1], key= lambda x: x[0])
                if index != len(stack):
                    ans[v[0]] = stack[index][1]
            
            # print(ans)
        # print(cache)
        return ans
    def check(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        ans = []
        for a, b in queries:
            s = max(a,b)
            curr = -1
            if a < b and heights[a] < heights[b]:
                ans.append(b)
            elif b < a and heights[b] < heights[a]:
                ans.append(a)
            elif a == b:
                ans.append(a)
            else:
                for i in range(s, n):
                    if heights[i] > heights[a] and  heights[i] > heights[b]:
                        curr = i
                        break
                ans.append(curr)
        print(*ans)
        return ans

    
heights = [6,4,8,5,2,7]
queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
# heights = [5,3,8,2,6,1,4,6]
# queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
heights = [1,2,1,2,1,2]
queries = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[5,0],[5,1],[5,2],[5,3],[5,4],[5,5]]

sol = Solution()
# sol.check(heights, queries)
print(sol.leftmostBuildingQueries(heights, queries))
