
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
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    # 45 / 931 个通过测试用例
    # 54 / 931 个通过测试用例
    # 57 / 931 个通过测试用例


    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:    
        @cache  # 记忆化搜索
        def dfs(i: int, mask: int, is_limit: bool, is_num: bool, nums):
            # print('dfs', i, mask)
            if i == len(nums):
                if is_num :
                    return 1
                else:
                    return 0
                # return int(is_num) 
            res = 0
            if not is_num:  # 可以跳过当前数位
                res = dfs(i + 1, mask, False, False, nums)
            low = 0 if is_num else 0  # 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
            up = min(int(nums[i]), limit) if is_limit else 9  # 如果前面填的数字都和 n 的一样，那么这一位至多填 s[i]（否则就超过 n 啦）
            for d in range(low, up + 1):  # 枚举要填入的数字 d
                res += dfs(i + 1, d , is_limit and d == up, True, nums)
            return res
        
        b = str(start)[0:len(str(start)) - len(s)]
        if len(b) > 0 and len(str(start)) >= len(s) and int(str(start)[len(str(start)) - len(s):]) < int(s):
            b = str(int(b) - 1)
        
        e = str(finish)[0:len(str(finish)) - len(s)]
        if len(e) > 0 and len(str(finish)) >= len(s) and int(str(finish)[len(str(finish)) - len(s):]) < int(s):
            e = str(int(e) - 1)
        
        res1 = dfs(0, 0, True, False, b)
        res2 = dfs(0, 0, True, False, e)
        if start > int(s) and len(str(start)) == len(s):
            res1 = 1
        
        print(b, e, res1, res2)
        
        return res2 - res1
       
    
start = 1
finish = 6000
limit = 4
s = "124"

start = 15
finish = 215
limit = 6
s = "10"

start = 1
finish = 971
limit = 9
s = "72"

start = 1000
finish = 2000
limit = 4
s = "3000"

start = 141
finish = 148
limit = 9
s = "9"

#22 == 8
start = 20
finish = 1159
limit = 5
s = "20"

sol = Solution()
print(sol.numberOfPowerfulInt(start, finish, limit, s))
