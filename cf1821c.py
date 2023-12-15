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
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main(s):
    #每次删一半，尽量保留最多的那个
    next = ''
    ans = 0
    while True:
        alpha = [0] * 26
        for v in s:
            alpha[ord(v) - 96] += 1
        # print(alpha)
        ma = 0
        mi = 0
        for i in range(26):
            if alpha[i] > ma:
                ma = alpha[i]
                mi = i
        if ma == len(s):
            break
        dst = chr(96 + mi)
        next = ''
        ans += 1
        i = 0
        last = -2
        # print('dst' , dst)
        while i < len(s):
            if (ma > 1 and s[i] == dst ) or i == last + 1:
                next += s[i]
            else:
                last = i
            i += 1
        # print('next ', next)
        s = next

    # print('ans ', ans)
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    s = input()
    main(s)
   
