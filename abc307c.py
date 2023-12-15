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

input = lambda: sys.stdin.readline().rstrip()
# input = lambda: sys.stdin.readline().rstrip()
sint = lambda :int(input())
mint = lambda :map(int,input().split())
lint = lambda :list(mint())


def solve(A,B,X):

    def getAllPoints(A):
        h = len(A)
        w = len(A[0])
        ap = []
        for i in range(h):
            for j in range(w):
                if A[i][j] == '#':
                    ap.append([i,j])
        offset = [ap[0][0], ap[0][1]]
        for v in ap:
            v[0] -= offset[0]
            v[1] -= offset[1]
        return ap
    
    def getPosition(ap,xp):
        ans = defaultdict()
        for vx in xp:
            used = defaultdict(int)
            diff = [vx[0] - ap[0][0], vx[1] - ap[0][1]]
            flag = True
            # print('A', vx, ap[0], diff)
            for i in range(1, len(ap)):
                next = (ap[i][0] + diff[0], ap[i][1] + diff[1])
                # print(vx, diff, next)
                if next in xp:
                    used[next] = 1
                else:
                    flag = False
                    break
            if flag == True:
                used[vx] = 1
                ans[vx] = used
        return ans

    ap = getAllPoints(A)
    bp = getAllPoints(B)
    xp = set([tuple(v) for v in getAllPoints(X)])
    
    apos = getPosition(ap, xp)
    bpos = getPosition(bp, xp)
    # print(apos, bpos)
    for av in apos:
        for bv in bpos:
            flag = True
            for xv in xp:
                if apos[av][xv] == 1 or bpos[bv][xv] == 1:
                    continue
                else:
                    flag = False
                    break
            if flag:
                print(YES)
                return
    print(NO) 
    
    return

h,w = lint()
A = []
for _ in range(h):
    A.append(input())

h,w = lint()
B = []
for _ in range(h):
    B.append(input())

h,w = lint()
X = []
for _ in range(h):
    X.append(input())

solve(A,B,X)


