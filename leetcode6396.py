
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
    def count2(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int: 
        num1 = int(num1)
        num2 = int(num2)
        def digit_sum(x):
            ret = 0
            while x > 0:
                ret += x%10
                x //= 10 
            return ret
        ans = 0
        for i in range(num1, num2+1):
            temp = digit_sum(i)
            if temp >= min_num and temp <= max_sum:
                ans += 1

        return ans%MOD
    
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int: 
        @cache  # 记忆化搜索
        def dfs(i: int, mask: int, is_limit: bool, is_num: bool, nums):
            # print('dfs', i, mask)
            if i == len(nums):
                if is_num and mask  >= min_sum and mask <= max_sum:
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
                if mask + d <= max_sum:
                    res += dfs(i + 1, mask + d , is_limit and d == up, True, nums)

            return res%MOD
        num1 = str(int(num1) - 1)
        res1 = dfs(0, 0, True, False, num1)
        res2 = dfs(0, 0, True, False, num2)  
        # print(res1, res2)    
        return (res2 + MOD - res1)%MOD

num1 = "1"
num2 = "12"
min_num = 1
max_num = 8
# num1 = "1"
# num2 = "5"
# min_num = 1
# max_num = 5
# num1 = "6312"
# num2 = "9416"
# min_num = 29
# max_num = 30
sol = Solution()
print(sol.count(num1, num2, min_num, max_num))
