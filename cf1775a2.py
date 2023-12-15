# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main(s):
    n = len(s)
    if s[0] == 'a' and s[n - 1] == 'a' or s[0] == 'b' and s[n - 1] == 'a':
        #find b
        for i in range(1,n-1):
            if s[i] == 'b':
                print(s[:i], s[i:n-1], s[n-1])
                return 
        #all a
        print(s[:1], s[1:n-1], s[n-1])
    elif s[0] == 'a' and s[n - 1] == 'b' or s[0] == 'b' and s[n - 1] == 'b':
        #find a
        for i in range(1,n-1):
            if s[i] == 'a':
                print(s[:i], s[i], s[i+1:])
                return 
        #all b
        print(s[:n-2], s[n-2], s[n-1])
    return 

s = 'baaaa'
main(s)
# caseNum = int(input())
# for i in range(0, caseNum):
#     s = input()
#     main(s)

a = [[1,2],[2,1,2],(3,2),(3,1)]
print(a)
a.sort(key=lambda x:(x[0]))
# a.sort(key=lambda x:(x[1]))
print(a)   
