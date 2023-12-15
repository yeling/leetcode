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

def solve(n, m, s, t):
    one = 0
    zero = 0
    if len(s) == 1:
        print(YES)
        return
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1] and s[i] == '0':
            zero += 1
        elif s[i] == s[i - 1] and s[i] == '1':
            one += 1
    tf = True
    for i in range(1, len(t)):
        if t[i] != t[i - 1]:
            continue
        else:
            tf = False
            break
        
    if zero == 0 and one == 0:
        print(YES)
    elif zero > 0 and one == 0:
        if t[0] == '1' and len(t)%2 == 1 and tf == True:
            print(YES)
        else:
            print(NO)
    elif zero == 0 and one > 0:
        if t[0] == '0' and len(t)%2 == 1 and tf == True:
            print(YES)
        else:
            print(NO)
    else:
        print(NO)
    

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    s = input()
    t = input()
    solve(n, m, s, t)

   
