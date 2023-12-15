
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
    # AC
    #dp[i] 前i个最低高度
    #dp[i + 1] 为 i + 1个到前面N个放同一层的最大高度
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [INF] * (n + 1)
        dp[0] = 0
        dp[1] = books[0][1] 
        for i in range(0,n):
            j = i
            total = 0
            currH = 0
            while j >= 0:
                total += books[j][0]
                if total <= shelfWidth:
                    currH = max(currH, books[j][1])
                    dp[i + 1] = min(dp[i + 1], dp[j] + currH)
                    j -= 1 
                else:
                    break
            # print(dp)

        return dp[n]
    
books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelfWidth = 4

books = [[1,3],[2,4],[3,2]]
shelfWidth = 6

sol = Solution()
print(sol.minHeightShelves(books, shelfWidth))
