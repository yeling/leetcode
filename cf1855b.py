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


def calc(k):
    ans = []
    for i in range(1,int(sqrt(k)) + 1):
        if k%i == 0:
            ans.append(i)
            if i != k//i:
                ans.append(k//i)
    return ans
#先暴力
def solve2(n):
    #
    temp = calc(n)
    temp.sort()
    ans = 1
    i,j = 0,0
    # print(temp)
    while i < len(temp):
        j = i + 1
        while j < len(temp) and temp[j] == temp[j - 1] + 1:
            j += 1
        ans = max(ans, j - i)
        i = j
    print(ans)
    return 

#纯数论题目，需要时1..x可以除
def solve(n):
    #
    ans = 1
    for i in range(1,n+2):
        if n%i != 0:
            print(i - 1)
            return
    # print(n)
    return 


caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    # solve2(n)
    solve(n)

   
