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


n = int(input())
s = input()
q = int(input())

#TLE
def solve2():
    cache = [[] for _ in range(26)]
    for i,v in enumerate(s):
        cache[ord(v) - ord('a')].append(i)
    for _ in range(q):
        t = input()
        c,d = t.split(' ')
        if c != d:
            cache[ord(d) - ord('a')] += cache[ord(c)- ord('a')]
            cache[ord(c) - ord('a')] = []
    all = []
    for i in range(26):
        for v in cache[i]:
            all.append((v, chr(i + 97)))
    all.sort()
    # print(all)
    ans = ''
    for i,v in all:
        ans += v
    print(ans)

    return

def solve():
    cache = [[] for _ in range(26)]
    for i,v in enumerate(s):
        cache[ord(v) - ord('a')].append(i)
    cache2 = [[i] for i in range(26)]
    for _ in range(q):
        t = input()
        c,d = t.split(' ')
        if c != d:
            cache2[ord(d) - ord('a')] += cache2[ord(c)- ord('a')]
            cache2[ord(c) - ord('a')] = []
    # print(cache2)
    dstCache = [[] for _ in range(26)]
    for i in range(26):
        for v in cache2[i]: 
            dstCache[i] += cache[v]
    all = []
    for i in range(26):
        for v in dstCache[i]:
            all.append((v, chr(i + 97)))
    all.sort()
    # print(all)
    ans = ''
    for i,v in all:
        ans += v
    print(ans)

    return

solve() 
# solve2() 
