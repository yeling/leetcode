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

def solve2(n, k, s, l, r, q, x):
    l.append(n + 1)
    # print(l, r)
    for v in x:
        pos = bisect_right(l,v)
        a = min(v, l[pos - 1] + r[pos - 1] - v) - 1
        b = max(v, l[pos - 1] + r[pos - 1] - v) - 1
        s = s[:a] + s[a:b+1][::-1] + s[b + 1:]
        # print(a,b)
    print(s)
    return 

#TLE
def solve(n, k, s, l, r, q, x):
    l.append(n + 1)
    # print(l, r)
    change = defaultdict(list)
    for v in x:
        pos = bisect_right(l,v)
        a = min(v, l[pos - 1] + r[pos - 1] - v) - 1
        b = max(v, l[pos - 1] + r[pos - 1] - v) - 1
        # print(a,b)
        change[(a + b)^MOD].append((a,b))
    # print("change", change)
    ans = [v for v in s]
    for k in change:
        temp = defaultdict(int)
        for v in change[k]:
            temp[v] += 1
        # print(temp)
        tempKey = list(temp.keys())
        tempKey.sort()
        # print(tempKey)
        left = 0
        l = -1
        for i in range(len(tempKey)):
            next = (left + temp[tempKey[i]])%2
            if (l != -1 and left != next and next == 0):
                a = l
                b = tempKey[i][0] - 1
                c = tempKey[i][1] + 1
                d = c + b - a
                # s = s[:a] + s[c:d+1][::-1] + s[b + 1: c] + s[a:b+1][::-1] + s[d+1:]
                for j in range(a, b + 1):
                    tempj = ans[j]
                    ans[j] = ans[d - (j - a)]
                    ans[d - (j - a)] = tempj
                
            if i == len(tempKey) - 1 and next == 1:
                if left == 1:
                    a = l
                    b = tempKey[i][1] + tempKey[i][0] - l
                else:
                    a = tempKey[i][0]
                    b = tempKey[i][1]
                # a = l                
                # s = s[:a] + s[a:b+1][::-1] + s[b + 1:]
                for j in range(a, a + (b - a)//2 + 1):
                    tempj = ans[j]
                    ans[j] = ans[b - (j - a)]
                    ans[b - (j - a)] = tempj

            if left == 1 and next == 0:
                l = -1
            elif left == 0 and next == 1:
                l = tempKey[i][0]

            left = next
            
    print(''.join(ans))
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    s = input()
    l = li()
    r = li()
    q = int(input())
    x = li()
    solve(n, k, s, l, r, q, x)

   
