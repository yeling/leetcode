# auther yeling
import sys
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from heapq import *
import string
from os import path

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

# for I/O for local system
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    # sys.stdout = open("output.txt","w")

# For fast I/O
# input = sys.stdin.buffer.readline
# input = sys.stdin.readline
# print = sys.stdout.write

input = lambda: sys.stdin.readline().rstrip()
si = lambda :int(input())
mi = lambda :map(int,input().split())
li = lambda :list(mi())

def solve(h, w, a, b):
    def cntSort(nums):
        ans = 0
        for i in range(len(nums)):
            for j in range(1, len(nums) - i):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    ans += 1
        return ans
    

    ans = INF
    for ph in permutations(range(h)):
        for pw in permutations(range(w)):
            flag = True
            for i in range(h):
                for j in range(w):
                    if b[i][j] == a[ph[i]][pw[j]]:
                        continue
                    else:
                        flag = False
                        break
                if flag == False:
                    break
            if flag:
                # print(ph, pw)
                cnt = 0
                cnt = cntSort(list(ph[:]))
                cnt += cntSort(list(pw[:]))
                ans = min(ans, cnt)
                
    if ans == INF:
        print(-1)
    else:
        print(ans)
    return

h,w = li()
a = []
for _ in range(h):
    a.append(li())
b = []
for _ in range(h):
    b.append(li())
solve(h, w, a, b)

