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

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main2(n, a, b):
    cnt = defaultdict(int)
    ans = [0] * n
    for i,v in enumerate(b):
        cnt[str(a[i])] += 1
        # print(cnt)
        next = defaultdict(int)
        for pre in list(cnt.keys()):
            if v >= int(pre):
                ans[i] += int(pre) * cnt[pre]
                del cnt[pre]
            else:
                ans[i] += v * cnt[pre]
                next[str(int(pre) - v)] += cnt[pre]
                del cnt[pre]
        cnt = next
        # print(cnt)
    print(*ans)
    return 

def main(n, a, b):
    cnt = defaultdict(int)
    ans = [0] * n
    for i,v in enumerate(b):
        cnt[str(a[i])] += 1
        # print(cnt)
        next = defaultdict(int)
        for pre in list(cnt.keys()):
            if v >= int(pre):
                ans[i] += int(pre) * cnt[pre]
                del cnt[pre]
            else:
                ans[i] += v * cnt[pre]
                next[str(int(pre) - v)] += cnt[pre]
                del cnt[pre]
        cnt = next
        # print(cnt)
    print(*ans)
    return 

# n = 3
# a = [10, 20, 15]
# b = [9, 8, 6]
# main(n, a, b)
caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    a = li()
    b = li()
    main(n, a, b)
   
