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
sint = lambda :int(input())
mint = lambda :map(int,input().split())
lint = lambda :list(mint())

def getAllFactor(num):
    ans = []
    i = 2
    while i * i <= num:
        if num % i == 0:
            ans.append(i)
            if i != num//i:
                ans.append(num//i)
        i += 1
    # ans.append(num)
    return ans

def solve(n):
    # print("input",n)
    f = getAllFactor(n)
    f.sort()
    # print(f)
    #
    for i in range(2,27):
        flag = True
        for v in f:
            if v%i == 0:
                flag = False
                break
        if flag:
            # print(i)
            ans = [chr(j + 97) for j in range(i)]*((n - 1)//i + 1)
            print(''.join(ans[:n]))
            return
            
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    solve(n)

   
