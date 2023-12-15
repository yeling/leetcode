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

def solve(n):
    # if n < 7:
    #     print(NO)
    #     return
    for i in range(2, int(sqrt(n)) + 2):
        temp = n
        k = 0
        while (temp - 1)%i == 0:
            temp -= 1
            temp //= i
            k += 1
        if temp == 0 and k > 2:
            print(YES)
            return
    print(NO)


    
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    solve(n)

   
