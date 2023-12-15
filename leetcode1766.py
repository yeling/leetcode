
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

class Solution:
    # 35 / 37 个通过的测试用例 TLE 10**5
    def getCoprimes2(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        n = len(nums)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        ans = [-1] * n
        def dfs(u, fa, path:List[int]):
            for i in range(len(path) - 2, -1, -1):
                if gcd(nums[u], nums[path[i]]) == 1:
                    ans[u] = path[i]
                    break
            for v in g[u]:
                if v != fa:
                    path.append(v)
                    dfs(v, u, path)
                    path.pop()
            return
        dfs(0, -1, [0])
        return ans
    # 29 / 37 个
    #AC
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        n = len(nums)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        ans = [-1] * n
        #key -> (index, depth) (index, depth)
        def dfs(u, fa, path:List[int], depth):
            
            for v in g[u]:
                if v != fa:
                    curr = 0
                    index = -1
                    # print(u, path, depth)
                    for i in range(1, len(path)):
                        if path[i] != -1 and gcd(nums[v], i) == 1:
                            if curr < path[i][1]:
                                curr = path[i][1]
                                index = path[i][0]
                    ans[v] = index
                    
                    pre = path[nums[v]]
                    path[nums[v]] = (v,depth + 1)
                    dfs(v, u, path, depth + 1)
                    path[nums[v]] = pre
            return
        #key [(index, depth)]
        path = [-1] * 51
        path[nums[0]] = (0,1)
        dfs(0, -1, path, 1)
        return ans
    
nums = [2,3,3,2]
edges = [[0,1],[1,2],[1,3]]

# nums = [5,6,10,2,3,6,15]
# edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]

# nums = [1]
# edges = []


sol = Solution()

print(sol.getCoprimes2(nums, edges))
print(sol.getCoprimes(nums, edges))

nums = [18,10,23,47,11,20,7,44,14,43,43,42,2,23,5,31,18,40,49,27,50,21,19,35,23,30,31,8,7,50,7,11,4,43,1,5,24,44,24,25,24,19,48,5,37,13,50,6,20,38,43,45,34,15,42,41,5,44,16,21,26,31,12,35,13,36,2,21,29,36,7,24,1,37,40,6,19,30,12,42,30,50,20,15,34,36,49,2,34,36,38,8,11,33,46,19,24,41,2,31,14,32,9,29,12,6,45,47,32,24,37,4,25,50,24,10,31,40,5,12,22,7,23,2,27,42,8,6,1,15,16,32,32,38,29,24,33,22,33,29,17]

n1 = [-1,61,87,97,62,-1,129,-1,13,121,108,10,122,30,58,31,68,122,14,8,19,132,140,90,15,-1,53,68,64,110,3,81,28,80,63,105,55,55,72,86,-1,29,13,70,75,114,76,26,-1,55,99,99,110,91,68,79,84,-1,61,123,-1,29,18,0,95,68,13,1,44,70,1,68,63,128,41,61,5,13,13,13,13,-1,124,49,50,76,93,39,-1,55,116,10,32,32,70,37,70,72,70,136,-1,112,66,74,61,68,18,65,-1,10,3,10,99,4,-1,70,65,138,91,-1,18,10,100,10,130,14,26,76,63,41,18,61,-1,10,93,55,29,129,18,130,1]
n2 = [-1,61,87,97,62,-1,129,-1,13,121,108,10,122,30,58,31,68,122,14,8,19,132,140,90,15,-1,53,68,64,110,3,81,28,80,63,105,55,55,72,86,-1,29,13,70,75,114,76,26,-1,55,99,99,110,91,68,79,84,-1,61,123,-1,29,18,0,95,68,13,1,44,70,1,68,34,128,41,61,5,13,13,13,13,-1,124,49,50,76,93,39,-1,55,116,10,32,32,70,37,70,72,70,136,-1,112,66,74,61,68,18,65,-1,10,3,10,99,4,-1,70,65,138,91,-1,18,10,100,10,130,14,26,76,63,41,18,61,-1,10,93,55,29,129,18,130,1]

for i in range(len(n1)):
    if n1[i] != n2[i]:
        print(i, n1[i], n2[i])
        print(nums[i], nums[n1[i]], nums[n2[i]])