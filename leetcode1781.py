
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
    def beautySum2(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i+3, n + 1):
                sub = s[i:j]
                cl = Counter(sub).most_common()
                ans += cl[0][1] - cl[-1][1]
                # print(i, cl, ans)
        return ans
    
    def beautySum3(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        for i in range(n):
            cache = defaultdict(int)
            for j in range(i, n):
                cache[s[j]] += 1
                if j - i >= 2:
                    big = -INF
                    small = INF
                    for k in cache:
                        temp = cache[k]
                        if temp < small:
                            small = temp
                        if temp > big:
                            big = temp
                    ans += big - small
                # print(i, cache, ans)
        return ans

    def beautySum4(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            cache = [0]*26
            for j in range(i, n):
                cache[ord(s[j]) - 97] += 1
                if j - i >= 2:
                    big = -INF
                    small = INF
                    for temp in cache:
                        if temp != 0:
                            if temp < small:
                                small = temp
                            if temp > big:
                                big = temp
                    ans += big - small
                # print(i, cache, ans)
        return ans
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            cnt = Counter()
            for j in range(i, n):
                cnt[s[j]] += 1
                ans += max(cnt.values()) - min(cnt.values())
                # print(i, cl, ans)
        return ans

s = "aabcb"
s = "aabcbaa"
s = "xzvfspps"
sol = Solution()
print(sol.beautySum2(s))
print(sol.beautySum(s))
