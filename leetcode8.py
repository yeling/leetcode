
# auther yeling
from typing import List
from bisect import *
from collections import *

MOD = 10 ** 9 + 7

class Solution:
    # 1077 / 1083
    def myAtoi(self, s: str) -> int:
        ne = False
        res = None
        for v in s:
            if v == ' ' and res == None:
                continue
            elif v == '+' and res == None:
                ne = False
                res = 0
            elif v == '-' and res == None:
                ne = True
                res = 0
            elif v >= '0' and v <= '9':
                if res == None:
                    res = int(v)
                    if ne:
                        res = -res
                else:
                    if not ne:
                        res = res * 10 + int(v)
                    else :
                        res = res * 10 - int(v)
                if res > 2 ** 31 - 1:
                    res = 2 ** 31 - 1
                    break
                elif res < -2 ** 31:
                    res = -2 ** 31
                    break
            else:
                break
        if res == None:
            res = 0
        return res




s = "-04-19.3 with words"
s = "   +0 123"
sol = Solution()
print(sol.myAtoi(s))
