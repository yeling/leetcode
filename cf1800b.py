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

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main(n, k, s):
    cnt = defaultdict(int)
    for v in s:
        cnt[v] += 1
    ans = 0
    for v in string.ascii_lowercase:
        ans += min(cnt[v], cnt[chr(ord(v) - 32)])
        diff = abs(cnt[v] -  cnt[chr(ord(v) - 32)])
        # print(v, diff, k)
        ans += min(k, diff // 2)
        k = max(0, k - diff // 2)
        
    print(ans)
    return 


caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    s = input()
    main(n, k, s)
   
