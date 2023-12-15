
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
    
    #126 / 138 个通过测试用例
    def takeCharacters2(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        n = len(s)
        pre = [[0]*3 for  _ in range(n)]
        after = [[0]*3 for  _ in range(n)]
        
        for i in range(n):
            if i > 0:
                pre[i] = pre[i-1][:]
                after[i] = after[i-1][:]
            pre[i][ord(s[i]) - 97] += 1
            after[i][ord(s[n-1-i]) - 97] += 1
        
        ans = INF
        for i,curr in enumerate(pre):
            temp = [INF] * 3
            for j in range(3):
                dst = k - curr[j]
                temp[j] = bisect_left(after, dst,hi = n - i , key=lambda x:x[j])
            th = max(temp[0], temp[1], temp[2])
            if th != n - i:
                ans = min(ans, th + i + 2)
        if ans == INF:
            ans = -1
        
        return ans
    
    # 126 / 138 个通过测试用例
    # 135 / 138 个通过测试用例
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        n = len(s)
        pre = [[0]*3 for  _ in range(n + 1)]
        after = [[0]*3 for  _ in range(n + 1)]
        
        for i in range(1,n+1):
            pre[i] = pre[i-1][:]
            after[i] = after[i-1][:]
            pre[i][ord(s[i - 1]) - 97] += 1
            after[i][ord(s[n- 1- i + 1]) - 97] += 1
        
        ans = INF
        for i,curr in enumerate(pre):
            temp = [INF] * 3
            for j in range(3):
                dst = k - curr[j]
                temp[j] = bisect_left(after, dst, hi = n - i+1, key=lambda x:x[j])
            th = max(temp[0], temp[1], temp[2])
            if th != n - i + 1:
                if i == 0:
                    ans = min(ans, th)
                else:
                    ans = min(ans, th + i)
        if ans == INF:
            ans = -1
        
        return ans
    
s = "aabaaaacaabc"
k = 2
# s = "a"
# k = 1
# s = "abc"
# k = 1
# s = "acccc"
# k = 4

s = "acba"
k = 1

# s = "a"
# k = 1

sol = Solution()
print(sol.takeCharacters(s,k))
# nums = [[1,0,0]]
# print(bisect_left(nums, 1, hi=1, key=lambda x:x[1]))
