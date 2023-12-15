
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue


MOD = 10 ** 9 + 7

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        cache = defaultdict(int)
        s = 0
        for v in skill:
            s += v
        
        ave = s * 2//n 
        print(ave)
        res = 0
        for v in skill:
            # print(cache)
            if cache[ave - v] != 0:
                cache[ave - v] -= 1
                res += v * (ave - v)
                if cache[ave - v] == 0:
                    del cache[ave - v]
            else:
                cache[v] += 1
        s = 0
        for k  in cache:
            s += cache[k]
        if s == 0:
            return res
        else:
            return -1
    
skill = [3,2,5,1,3,4]
skill = [1,1,2,3]
skill = [3,4]
sol = Solution()
print(sol.dividePlayers(skill))
