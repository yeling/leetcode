
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    # TLE
    def smallestRepunitDivByK2(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        curr = 1
        while curr % k != 0:
            curr = curr * 10 + 1
        # print(curr, curr//k, len(str(curr)))
        return len(str(curr))


    # AC
    def smallestRepunitDivByK3(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        #1 11特殊处理
        if str(k).count('1') == len(str(k)):
            return len(str(k))
        # 1, 3, 7, 9
        ans = []
        b = []
        temp = k
        while temp > 0:
            b.append(temp%10)
            temp //= 10
        # print(b)

        a = []
        i = 0
        left = 0
        while True:
            flag = False
            for j in range(0,10):
                curr = j * b[0] + left
                if curr % 10 == 1:
                    flag = True
                    a.append(j)
                    ans.append(1)
                    break
            if flag == False:
                return -1
            left = curr//10
            # left = (a[-1] * b[i])
            for j in range(i+1):
                if j + 1 < len(b):
                    left += a[-1 - j] * b[j+1]
                else:
                    break
            
            i += 1
            if left == 0 and i > len(b):
                break
            # print(left, a)
        # print(b, a,  ans)

        return len(ans)
    
    # mod
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        ans = 1
        cnt = 1
        while True:
            if ans % k == 0:
                break
            else:
                ans = ans % k
                ans = ans * 10 + 1
            cnt += 1
        return cnt
    
k = 3
sol = Solution()
# print(sol.smallestRepunitDivByK(111))
k = 3991
print(sol.smallestRepunitDivByK2(k))
# 39 2849
print(sol.smallestRepunitDivByK(k))

