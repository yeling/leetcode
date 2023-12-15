
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue


# 2151. 基于陈述统计最多好人数
# 1.因为2 <= n <= 15，枚举所有可能性，找出最大值
# 2 ** n 状态压缩
# 数位DP问题？？

MOD = 10 ** 9 + 7

class Solution:
    # AC
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        res = 0
        for i in range(1, 2 ** n):
            temp = [0] * n
            ti = i
            for j in range(n):
                if ti & 1 == 1:
                    temp[n-1-j] = 1
                ti >>= 1
            pa = True
            for j in range(n):
                if temp[j] == 1:
                    for k in range(n):
                        if statements[j][k] == 0 and temp[k] == 1:
                            pa = False
                            break
                        elif statements[j][k] == 1 and temp[k] == 0:
                            pa = False
                            break
            if pa:
                res = max(res, temp.count(1))
        return res
    
statements = [[2,1,2],[1,2,2],[2,0,2]]
sol = Solution()
print(sol.maximumGood(statements))
