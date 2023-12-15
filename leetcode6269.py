
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
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = INF
        for i,v in enumerate(words):
            if v == target:
                if i <= startIndex:
                    ans = min(ans, abs(i - startIndex), n + i - startIndex)
                else:
                    ans = min(ans, abs(i - startIndex), n + startIndex - i)
        if ans == INF:
            ans = -1
        return ans
    
words = ["a","b","leetcode"]
target = "leetcode"
startIndex = 0
# words = ["a","b","leetcode"]
# target = "leetcode"
# startIndex = 0

# words = ["i","eat","leetcode"]
# target = "ate"
# startIndex = 0


# words = ["hello","i","am","leetcode","hello"]
# target = "hello"
# startIndex = 1

sol = Solution()
print(sol.closetTarget(words, target, startIndex))
