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
YES="YES"
NO="NO"


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

def solve2(s):
    cnt = 0
    upcnt = 0
    middle = 0
    for v in s:
        if v == '+':
            cnt += 1
            middle += 1
        elif v == '-':
            cnt -= 1
            middle -= 1
        elif v == '0':
            if cnt == upcnt:
                print(NO)
                return
        elif v == '1':
            if cnt != upcnt:
                print(NO)
                return
            # cnt = upcnt
        if upcnt < 1 or upcnt > cnt:
            print(NO)
            return
    print(YES)

    return 

def solve(s):
    cnt = 0
    # 正序的位置
    s1 = 1
    # 乱序的位置
    s2 = INF
    for v in s:
        if v == '+':
            cnt += 1
        elif v == '-':
            cnt -= 1
            if s1 > cnt:
                s1 = max(1,cnt)
            if s2 > cnt:
                s2 = INF
        elif v == '0':
            s2 = min(s2,cnt)
            if s1 >= cnt:
                print(NO)
                return
        elif v == '1':
            s1 = max(s1, cnt)
            if s2 <= cnt:
                print(NO)
                return
            
    print(YES)
    return

caseNum = int(input())
for i in range(0, caseNum):
    s = input()
    solve(s)

   
