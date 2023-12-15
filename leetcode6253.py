
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
    def isCircularSentence(self, sentence: str) -> bool:
        arr = sentence.split(' ')
        n = len(arr)
        curr = arr[0]
        if arr[-1][-1] != curr[0]:
            return False
        for i in range(1,n):
            # print(curr)
            if arr[i][0] != curr[-1]:
                return False
            curr = arr[i]
        return True
    

sentence = "leetcode exercises sound delightful"
sentence = "ete axercisee"
sol = Solution()
print(sol.isCircularSentence(sentence))
