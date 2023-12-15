
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        cache = defaultdict(int)
        for v in sentence:
            cache[v] +=1
        for v in string.ascii_lowercase:
            if cache[v] == 0:
                return False    
        return True
    

sol = Solution()
sentence = "thequickbrownfoxjumpsoverthelazydog"
sentence = "leetcode"
print(sol.checkIfPangram(sentence))
