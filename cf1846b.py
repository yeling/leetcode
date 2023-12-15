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

def solve(grid):
    # print(grid)
    def find(sym):
        #row
        for i in range(3):
            if grid[i].count(sym) == 3:
                return True
        #col
        for i in range(3):
            if grid[0][i] == sym and grid[1][i] == sym and grid[2][i] == sym :
                return True
        #xie
        if grid[0][0] == sym and grid[1][1] == sym and grid[2][2] == sym :
            return True
        if grid[0][2] == sym and grid[1][1] == sym and grid[2][0] == sym :
            return True
        return False
    a = find('X')
    b = find('O')
    c = find('+') 
    # print(a, b, c)
    if a == True and b == False and c == False:
        print('X')
        return
    if a == False and b == True and c == False:
        print('O')
        return
    if a == False and b == False and c == True:
        print('+')
        return
    print("DRAW")
    
    
    return 

caseNum = int(input())
for i in range(0, caseNum):
    grid = []
    for _ in range(3):
        grid.append(input())
    solve(grid)

   
