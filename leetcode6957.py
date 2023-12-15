
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
    # 46 / 2522 个通过测试用例
    # 48 / 2522 个通过测试用例
    def countSteppingNumbers2(self, low: str, high: str) -> int: 
        
        def check(s):
            # 0 - 9结尾的数字
            if len(s) == 1:
                return s[0]
            dp = [1]*10
            ans = [1]*10
            ans[0] = 0

            n = len(s)
            preLimit = s[-1]
            for i in range(n - 2, -1, -1):
                # next = dp[:]
                next = [0]*10
                l,r = 0,9
                if i == 0:
                    l = 1
                    r = s[i] + 1

                for j in range(l, r):
                    if j == s[i]:
                        if j == 0 and preLimit >= 1:
                            next[j] += dp[j + 1]
                        elif j == 9 and preLimit >= 8:
                            next[j] += dp[j - 1] 
                        else:
                            if preLimit >= j + 1:
                                next[j] += dp[j - 1] + dp[j + 1]
                            elif preLimit >= j - 1:
                                next[j] += dp[j - 1] 
                    else:
                        if j == 0:
                            next[j] += dp[j + 1]
                        elif j == 9:
                            next[j] += dp[j - 1] 
                        else:
                            next[j] += dp[j - 1] + dp[j + 1]
                    next[j] %= MOD
                preLimit = s[i]
                for k in range(10):
                    ans[k] += next[k]
                dp = next
            # ans = sum(dp) - dp[0]
            # print(ans)
            return sum(ans)
            # return ans

        lows = [int(v) for v in low]   
        highs =  [int(v) for v in high]   
        l = check(lows)
        h = check(highs)
        flag = True
        for i in range(1, len(lows)):
            if abs(lows[i] - lows[i - 1]) != 1:
                flag = False
                break
        if len(lows) == 1:
            flag = True

        if flag:
            ans = h - l + 1
        else:
            ans = h - l
        print(l, h)
        return ans
    
    #数位DP模版， 从高位到低位的计算
    def countSteppingNumbers(self, low: str, high: str) -> int: 
        @cache  # 记忆化搜索
        def dfs(i: int, mask: int, is_limit: bool, is_num: bool, nums):
            # print('dfs', i, mask)
            if i == len(nums):
                if is_num:
                    return 1
                else:
                    return 0
                # return int(is_num) 
            res = 0
            if not is_num:  # 可以跳过当前数位
                res = dfs(i + 1, mask, False, False, nums)
            low = 0 if is_num else 1  # 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
            up = int(nums[i]) if is_limit else 9  # 如果前面填的数字都和 n 的一样，那么这一位至多填 s[i]（否则就超过 n 啦）
            for d in range(low, up + 1):  # 枚举要填入的数字 d
                if mask == -1 or abs(d - mask) == 1:
                    res += dfs(i + 1, d , is_limit and d == up, True, nums)
                    res%MOD

            return res%MOD
        
        l = dfs(0, -1, True, False, low)
        # h = 0
        h = dfs(0, -1, True, False, high)

        lows = [int(v) for v in low]   
        flag = True
        for i in range(1, len(lows)):
            if abs(lows[i] - lows[i - 1]) != 1:
                flag = False
                break
        if len(lows) == 1:
            flag = True

        if flag:
            ans = h + MOD - l + 1
        else:
            ans = h + MOD - l
        # print(l, h)
        return ans%MOD
    
    
#14
#16
low = "20"
high = "111"
sol = Solution()
print(sol.countSteppingNumbers(low, high))
