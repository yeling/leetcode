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
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())


def main(n, k, s):
    if s.count(s[0]) == len(s):
        print(YES)
        return
    else:
        #三分成立
        if n%3 != 0:
            print(NO)
            return
        sub = n//3
        if k % sub != 0:
            print(NO)
            return
        
        s1 = s[:n//3]
        s2 = s[n//3:n//3 * 2]
        s3 = s[:n//3]
        # print(s1, s2, s3)
        for i in range(sub):
            if s1[i] == s2[-(1 + i)] and  s1[i] == s3[i]:
                continue
            else:
                print(NO)
                return
        print(YES)

# print(71630165869626180%12)
caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    s = input()
    main(n, k, s)

