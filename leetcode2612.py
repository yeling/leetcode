
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
    # 610 / 711 
    # 676 / 711 
    # 694 / 711 个通过的测试用例 TLE BFS
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        ans = [-2] * n
        for v in banned:
            ans[v] = -1
        ans[p] = 0
        #bfs
        stack = list()
        stack.append(p)
        t = 1
        layer = 1
        while len(stack) > 0:
            cnt = len(stack)
            layer += 1
            for i in range(cnt):
                curr = stack[i]
                l = curr - (k - 1)
                if l < 0:
                    l = l % 2
                r = curr + (k - 1)
                if r > n - 1:
                    r = n - 1 - r%2
                for i in range(l,r+1,2):
                    t += 1
                    start = 0
                    end = n - 1
                    if i > curr:
                        start = curr - ((k - 1) - (i - curr))//2
                        end = i + ((k - 1) - (i - curr))//2
                    else:
                        start = i - ((k - 1) - (curr - i))//2
                        end = curr + ((k - 1) - (curr - i))//2
                    if ans[i] == -2 and start >= 0 and end <= n - 1:
                        ans[i] = ans[curr] + 1
                        stack.append(i)
                print(curr, ans, t, layer)
            stack = stack[cnt:]
        for i,v in enumerate(ans):
            if v == -2:
                ans[i] = -1
        return ans

n = 4
p = 2
banned = [0,1,3]
k = 1
# print(-1%2)
n = 4
p = 0
banned = []
k = 4

n = 20
p = 7
banned = [8,0,5]
k = 10

sol = Solution()
print(sol.minReverseOperations(n, p, banned, k))
