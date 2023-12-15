
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def longestDecomposition(self, text: str) -> int:
        ans = 0
        n = len(text)
        l = 0
        r = n
        while l < (n + 1)//2:
            k = 1
            flag = False
            while l + k <= (n + 1)//2:
                if text[l:l+k] == text[r - k:r]:
                    # print(text[l:l+k])
                    if l + k == r:
                        ans += 1
                    else:
                        ans += 2
                    l = l + k
                    r = r - k
                    flag = True
                    break
                k += 1
            if flag:
                k = 0
            if l + k >= (n + 1)//2:
                if flag == False:
                    ans += 1
                break 
        return ans
    

text = "ghiabcdefhelloadamhelloabcdefghi"
text = "dacbacd"
sol = Solution()
print(sol.longestDecomposition(text))
