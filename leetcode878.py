
# auther yeling
from typing import List
from bisect import *
from collections import *
from math import *

MOD = 10 ** 9 + 7

class Solution:
    def nthMagicalNumber2(self, n: int, a: int, b: int) -> int:
        g = gcd(a,b)
        lcm = a * b / g
        # print(lcm)
        r = max(a,b) * n
        l = min(a,b)
        # delta = min(a,b)
        while l < r:
            m = (l + r) >> 1
            s = m // a + m // b - m // lcm
            # print(l, r, m, s)
            if s >= n:
                # r = m - 1
                r = m - min(m%a, m%b)
            else:
                # l = m + 1
                l = m + min(a - m%a, b - m%b)
        return l%MOD

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        g = gcd(a,b)
        c = a * b / g
        # print(lcm)
        r = min(a,b) * n
        l = min(a,b)
        # delta = min(a,b)
        while l <= r:
            m = (l + r) // 2
            s = m // a + m // b - m // c
            print(l, r, m, s)
            if s >= n:
                r = m - 1
            else:
                l = m + 1
                
        return (r + 1)%MOD
    
    # def nthMagicalNumber3(self, n: int, a: int, b: int) -> int:
    #     MOD = 10 ** 9 + 7
    #     l = min(a, b)
    #     r = n * min(a, b)
    #     g = gcd(a,b)
    #     c = a * b / g
    #     while l <= r:
    #         mid = (l + r) // 2
    #         cnt = mid // a + mid // b - mid // c
    #         if cnt >= n:
    #             r = mid - 1
    #         else:
    #             l = mid + 1
    #     return (r + 1) % MOD


# n = 4
# a = 2
# b = 3
n = 2
a = 10
b = 5
sol = Solution()
print(sol.nthMagicalNumber(n,a,b))
print(sol.nthMagicalNumber3(n,a,b))
