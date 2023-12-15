
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
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = 0
        n = len(blocks)
        cntw = 0
        ans = n
        print(n)
        while right < n:
            if right < k:
                if blocks[right] == 'W':
                    cntw += 1
                right += 1
            else:
                ans = min(ans, cntw)
                if blocks[right] == 'W':
                    cntw += 1
                if blocks[left] == 'W':
                    cntw -= 1
                right += 1
                left += 1
                print(left, right, cntw)
        ans = min(ans, cntw)
        return ans
        
    
blocks = "BBBBBWWBBWBWBWWWBWBWBBBBWBBBBWBWBWBWBWWBWWBWBWWWWBBWWWWBWWWWBWBBWBBWBBWWW"
blocks = "BBBBBWWBBWBWBWWWBWBWBBBBWBBBBW"
k = 29

# blocks = "WBBWWBBWBW"
# k = 7
sol = Solution()
print(sol.minimumRecolors(blocks, k))
