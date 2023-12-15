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

def solve(n, s):
    cache = s.split(" ")
    ans = [0] * n
    # print(cache)
    for v in cache:
        if v.count(' ') != len(v):
            ans[int(v[-1]) - 1] = v[0:len(v) -1]
    print(" ".join(ans))
    return 

def solve2(n, s):
    ans = defaultdict(str)
    # print(cache)
    i = 0
    while i < len(s):
        while i < len(s) and s[i] == ' ':
            i += 1
        temp = ''
        while i < len(s) and s[i] != ' ':
            temp += s[i]
            i += 1  
        # print(temp)
        index = ''
        for j in range(len(temp) - 1, -1, -1):
            if ord(temp[j]) >= 48 and ord(temp[j]) <= 57:
                continue
            else:
                index = temp[j + 1:]
                break
        ans[int(index) - 1] = temp[0:len(temp) - len(index)]
    ret = ""
    ks = list(ans.keys())
    ks.sort()
    for k in ks:
        ret += ans[k] + " "
    print(ret)
    return 

# print(ord("9"))
n = int(input())
s = input()
solve2(n, s)
   
