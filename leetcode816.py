
# auther yeling
from typing import List
from itertools import product
import math

# 增加逗号，或者点，使得两个数字合法
# 1个逗号，多个点


class Solution:
    res = []

    def valid(self, num):
        # 前置只能有1个零
        if num == None:
            return False
        if len(num) >= 2 and num[0] == '0' and num[1] != '.':
            return False
        pos = num.find('.')
        if pos != -1 and num[-1] == '0' or pos == len(num) - 1 or pos == 0:
            return False
        return True

    def dfs(self, index, num1, pre, str):
        if len(pre) >= 2 and pre[0] == '0' and pre[1] != '.':
            return

        if index == len(str):
            if num1 != None:
                num2 = pre
                if self.valid(num2) and self.valid(num1):
                    self.res.append('(' + num1 + ', ' + num2 + ')')
            return

        # 结束do nothing
        pre += str[index]
        self.dfs(index + 1, num1, pre, str)
        pre = pre[0: -1]
        # 增加逗号
        if num1 == None and self.valid(pre):            
            self.dfs(index, pre, '', str)
        # 增加点
        if '.' not in pre:
            pre += '.'
            self.dfs(index, num1, pre, str)

        return

    def ambiguousCoordinates(self, s: str) -> List[str]:
        self.res = []
        s = s[1:-1]
        self.dfs(0, None, '', s)
        return self.res

sol = Solution()
str = "(0123)"
# str = "(123)"
# str = "(100)"
# print(sol.ambiguousCoordinates(str))

a = [i for i in range(10)]
b = [i for i in range(20)]
print(a, b)
for i,j in product(a, b):
    print(i, j)

