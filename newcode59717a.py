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
sint = lambda :int(input())
mint = lambda :map(int,input().split())
lint = lambda :list(mint())

def isPrime(n):
    if(n == 1):
        return False
    m = int(sqrt(n))
    for i in range(2,m + 1):
        if n%i == 0:
            return False
    return True

def solve(s):
    n = len(s)
    for i in range(n):
        temp = int(s[0:n-i])
        # print(temp)
        if isPrime(temp) == False:
            print(NO)
            return

    print(YES)




    return 

caseNum = int(input())
for i in range(0, caseNum):
    s = input()
    solve(s)

   
