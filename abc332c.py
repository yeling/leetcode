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



def solve(n, m, s):
    # print(n)
    sn = len(s)
    i = 0
    ans = 0
    while i < sn:
        while i < sn and s[i] == '0':
            i += 1
        one = 0
        two = 0
        while i < sn and s[i] != '0':
            if s[i] == '1':
                one += 1
            elif s[i] == '2':
                two += 1 
            i += 1
        ans = max(ans, two, one + two - m)
        i += 1
    print(ans)
        
       
    return

n,m = li()
s = input()
solve(n, m, s)

