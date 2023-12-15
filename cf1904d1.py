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

def solve2(n, a, b):
    #(l,r)
    pos = [[-1,-1] for i in range(n)]
    for i in range(n):
        if a[i] > b[i]:
            print(NO)
            return
        for j in range(i, -1, -1):
            if a[j] > b[i]:
                break
            elif a[j] == b[i]:
                pos[i][0] = j
                break
        for j in range(i,n):
            if a[j] > b[i]:
                break
            elif a[j] == b[i]:
                pos[i][1] = j
                break
    flag = True
    for i in range(0,n):
        if pos[i][0] == -1 and pos[i][1] == -1:
            flag = False
            break
        if i == 0:
            continue
        
        if pos[i][1] != -1 and pos[i - 1][1] != -1:
            if pos[i][1] >= pos[i - 1][1]:
                continue
            else:
                flag = False
                break
        elif pos[i][0] != -1 and pos[i - 1][0] != -1:
            if pos[i][0] >= pos[i - 1][0]:
                continue
            else:
                flag = False
                break
        elif pos[i - 1][0] == -1 and pos[i - 1][1] != -1 and pos[i][0] != -1 and pos[i][1] != -1:
            flag = False
            break
            
    # print(pos)
    if flag:
        print(YES)
    else:
        print(NO)


    return 

# 从左右往中间发展
def solve(n, a, b):

    return

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    a = li()
    b = li()
    solve(n, a, b)

   
