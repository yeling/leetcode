
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

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    # 59 / 60
    # AC
    def maxRepOpt1(self, text: str) -> int:
        cnt = Counter(text)
        l = 0
        r = 0
        ans = 0
        n = len(text)
        tempCnt = Counter()
        #合法性验证, l,r 只有1种选择，或者两种选择，有一个长度为1
        def check(tempCnt:Counter):
            flag = False
            if len(tempCnt) == 1:
                flag = True
            elif len(tempCnt) == 2:
                allk = list(tempCnt.keys())
                if tempCnt[allk[0]] == 1 or tempCnt[allk[1]] == 1:
                    flag = True
            return flag
        
        while r < n:
            #合法性验证, l,r 只有1种选择，或者两种选择，有一个长度为1
            while r < n:
                # print(l, r, tempCnt, ans)
                tempCnt[text[r]] += 1
                if check(tempCnt):
                    if cnt[tempCnt.most_common(1)[0][0]] >= r - l + 1:
                        ans = max(ans, r - l + 1)
                    else:
                        ans = max(ans, r - l)
                    r += 1
                else:
                    if tempCnt[text[r]] == 1:
                        del tempCnt[text[r]]
                    else:
                        tempCnt[text[r]] -= 1
                    break
            while l < r:
                if tempCnt[text[l]] == 1:
                    del tempCnt[text[l]]
                else:
                    tempCnt[text[l]] -= 1
                l += 1
                if check(tempCnt):
                    break
            
            # print(tempCnt)


        return ans
    
# text = "cdebaaaba"
text = "ahhhdhjiah"
sol = Solution()
print(sol.maxRepOpt1(text))
