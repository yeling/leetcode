
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
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        nums = []
        ans = []
        for i,v in enumerate(words):
            if v != "prev":
                nums.append(int(v))
            else:
                k = 0
                j = i
                while j >= 0 and words[j] == "prev":
                    k += 1
                    j -= 1
                if k > len(nums):
                    ans.append(-1)
                else:
                    ans.append(nums[-k])


        return ans
    
words = ["1","2","prev","prev","prev"]
words = ["1","prev","2","prev","prev"]
sol = Solution()
print(sol.lastVisitedIntegers(words))
