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

cache = [1,3,6,10,15,21,28,36,45,55]
def solve(n):
    ans = 1
    t = n
    while t > 0:
        ans *= cache[t%10]
        t//= 10
    print(ans)
    
    return 

def check(n):
    ans = 0
    def digSum(t):
        ret = 0
        while t > 0:
            ret += t%10
            t //= 10
        return ret
    
    tar = digSum(n)
    
    for i in range(0,n+1):
        for j in range(0, n+1):
            if i + j <= n:
                a,b,c = i,j,n - i - j
                if digSum(a) + digSum(b) + digSum(c) == tar:
                    ans += 1
    print(ans)

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    # check(n)
    solve(n)
    

   
