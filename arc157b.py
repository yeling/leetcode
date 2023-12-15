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
    cx = s.count('X')
    n = len(s)
    ans = 0
    if k > cx:
        dst = k - cx
        l = 0
        ly = 0
        r = n - 1
        ry = n
        temp = 0
        while l < r and temp < dst:
            if s[l] == 'Y':
                temp += 1
                ly = l
            if temp == dst:
                ans = ry - l - 1 - 1
                break
            l += 1
            if s[r] == 'Y':
                temp += 1
            if temp == dst:
                ans = r - 1 - ly - 1
                break
            r -= 1
        print(ans)
    elif k == cx:
        print(n -1)
    else:
        l = 0
        r = 0
        cnt = 0
        while r < n:
            while r < n and cnt < k:
                if s[r] == 'X':
                    cnt += 1
                r += 1
            ans = max(r - l + 1)
            


n = 5
k = 3
s = 'XYXYX'
main(n, k, s)

# n,k = li()
# s = input()
# main(n, k, s)

