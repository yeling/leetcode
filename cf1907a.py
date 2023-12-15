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

def solve(s):
    r = s[0]
    c = s[1]
    row = ['a','b','c','d','e','f','g','h']
    for s in row:
        if s != r:
            print(s + c)
    for i in range(1,9):
        if i != int(c):
            print(r+str(i))

    return 

caseNum = int(input())
for i in range(0, caseNum):
    s = input()
    solve(s)

   
