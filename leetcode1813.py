
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
    # 127 / 137
    # 98 / 137 
    # 129 / 137
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s = sentence1.split(' ')
        b = sentence2.split(' ')
        i,j = 0,0
        while i < len(s) and i < len(b) and s[i] == b[i]:
            i += 1
        while j < len(s) - i and j < len(b) - i and s[-j - 1] == b[-j - 1]:
            j += 1
        return i + j == min(len(s), len(b))
            
sentence1 = "Y ggUFOmtf woKuTtO W uwJZ Zan wgm zprl Kgn mAY xLlCH phA UIVKIohfw al g m"
sentence2 = "Jfa jfvmGU bKSSX uQ AmTzbBW EF jdc ft Z g VcM oNlI jeX q mNG YnUgGSnejt Y"
# sentence1 = "A"
# sentence2 = "a A b A"
sentence1 = "of"
sentence2 = "of a"
sol = Solution()
print(sol.areSentencesSimilar(sentence1, sentence2))
