
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
    # 758 / 759 个通过的测试用例
    # AC,可以改成滑动窗口，o(26n)，窗口大小为k 2*k 26*k
    # 改成Counter会更快
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        ans = 0
        n = len(word)
        pre = [[0]*26 for _ in range(n + 1)]
        s = 0
        for i,v in enumerate(word):
            if i > 0 and abs(ord(word[i]) - ord(word[i - 1])) > 2:
                s = i
            pre[i + 1] = pre[i][:]
            pre[i + 1][ord(v) - ord('a')] += 1
            for j in range(1,27):
                check = i - j * k + 1
                if check < s:
                    break
                flag = True
                for jk in range(26):
                    diff = pre[i+1][jk] - pre[check][jk]
                    if diff == k or diff == 0:
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    ans += 1
                    # print(i, j)
        return ans
    
word = "igigee"
k = 2
# word = "aaabbbccc"
# k = 3
sol = Solution()
print(sol.countCompleteSubstrings(word,k))
