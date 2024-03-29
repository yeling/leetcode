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
from sys import stdout

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"


# for I/O for local system
# if(path.exists('input.txt')):
#     sys.stdin = open("input.txt","r")
    # sys.stdout = open("output.txt","w")

# For fast I/O
# input = sys.stdin.buffer.readline
# input = sys.stdin.readline
# print = sys.stdout.write

input = lambda: sys.stdin.readline().rstrip()
si = lambda :int(input())
mi = lambda :map(int,input().split())
li = lambda :list(mi())


caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    print("? 1 1")
    stdout.flush()
    d1 = int(input())
    print("?", 1, m)
    stdout.flush()
    d2 = int(input())
    x = (d1 + d2 + 3 - m)//2
    y = d1 + 2 - x
    if n == 1 or m == 1:
        print("?", 1, d1)
        stdout.flush()
        continue
    d3 = 10
    if x > 0 and y > 0:
        print("?", x, y)
        stdout.flush()
        d3 = int(input())

    if d3 == 0:
        print("!", x, y)
        stdout.flush()
    else:
        print("?", n, 1)
        stdout.flush()
        d3 = int(input())
        y = (d1 + d3 + 3 - n)//2
        x = d1 + 2 - y
        print("!", x , y)
        stdout.flush()




    
    
   
