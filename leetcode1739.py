
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
    # 56 / 86
    def minimumBoxes2(self, n: int) -> int:
        def base(h):
            base = 0
            all = 0
            for i in range(1,h + 1):
                base += i
                all += base
                # print(i, base, all)
            return all
        # def base(h):
        #      return h

        left = 0
        right = n
        target = n
        while left <= right:
                mid = left + (right - left)//2
                curr = base(mid)
                if target < curr:
                    right = mid - 1
                elif target >= curr:
                    left = mid + 1
        # print(left, right)
        #left
        s = base(right)
        if s == n:
            return (1 + right) * right//2
        else:
            diff = n - s
            # diff 还需要二分 n * (n + 1) // 2
            ans = (1 + right) * right//2
            delta = int(sqrt(diff))
            while delta * (delta + 1) // 2 < diff:
                delta += 1
            return ans + delta

    # 56 / 86
    def minimumBoxes(self, n: int) -> int:
        def base(h):
            base = 0
            all = 0
            for i in range(1,h + 1):
                base += i
                all += base
                # print(i, base, all)
            return all
        # def base(h):
        #      return h

        left = 0
        right = int(sqrt(n))
        target = n
        while left <= right:
            mid = left + (right - left)//2
            # print(mid)
            curr = base(mid)
            if target < curr:
                right = mid - 1
            elif target >= curr:
                left = mid + 1
        # print(left, right)
        #left
        s = base(right)
        if s == n:
            return (1 + right) * right//2
        else:
            diff = n - s
            # diff 还需要二分 n * (n + 1) // 2
            ans = (1 + right) * right//2
            delta = int(sqrt(diff))
            while delta * (delta + 1) // 2 < diff:
                delta += 1
            return ans + delta
    
n = 30
n = 119922115
sol = Solution()
print(sol.minimumBoxes(n))
