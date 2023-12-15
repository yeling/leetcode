
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
    def minLength(self, s: str) -> int:   
        while True:
            flag = False
            if 'AB' in s:
                pos = s.find('AB')
                s = s[0:pos] + s[pos+2:]
                flag = True
                # print(s) 
            if 'CD' in s:
                pos = s.find('CD')
                s = s[0:pos] + s[pos+2:]
                # print(s) 
                flag = True
            if flag == False:
                break
            
        return len(s)
    
s = "ABFCACDB"
sol = Solution()
print(sol.minLength(s))
