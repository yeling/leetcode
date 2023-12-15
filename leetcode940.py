
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue


# 940. 不同的子序列 II
# dp问题，找到前面一个相同的字母，
# 字母前面没出现过，等于前面的组合+（前面的组合,当前元素） + 当前元素
# 字母前面出现过，等于 前面的组合 + (前面的组合,当前元素）- (之前字母的前一个,当前元素)
# dp[i] = dp[i-1] + dp[i-1] +
MOD = 10 ** 9 + 7

class Solution:
    # 57 / 110 
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        dp = [0] * n
        dp[0] = 1
        cache = [list() for _ in range(26)]
        # print(cache)
        for i,v in enumerate(s):
            dp[i] = (dp[i - 1] + dp[i - 1] + 1)%MOD
            pre = cache[ord(v) - 97]
            if len(pre) > 0:
                if pre[-1] == 0:
                    dp[i] = (dp[i] - 1 + MOD)%MOD
                else:
                    dp[i] = (dp[i] - dp[pre[-1] - 1] - 1 + MOD)%MOD
            cache[ord(v) - 97].append(i)

            # print(dp)
        return dp[n - 1]%MOD
s = "aba"
s = "abc"
s = "abaa"
s = "abacaab"
s = "ab"
sol = Solution()
print(sol.distinctSubseqII(s))
