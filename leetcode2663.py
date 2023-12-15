
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:  
        ans = [ord(v) for v in s]
        ma = ord('a') + k - 1
        r = len(s) - 1
        while True:
            flag = False
            selct = ans[r]
            if ans[r] < ma:
                print(s[r] + 1)
                break


            break

        return ''.join([chr(v) for v in ans])
    
s = "abcz"
k = 26
sol = Solution()
print(sol.smallestBeautifulString(s,k))
