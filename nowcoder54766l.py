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

def main(a, b):
    ac = 0
    bc = 0
    n = len(a)
    for i in range(n):
        # print(i, ac,bc)
        if i < 5:
            if a[i] == 1:
                ac += 1
            if abs(ac - bc) > 5 - 1 - i:
                print(i+1)
                print(str(ac) + ":" + str(bc))
                return 
            if b[i] == 1:
                bc += 1
            if abs(ac - bc) > 5 - 1 - i:
                print(i+1)
                print(str(ac) + ":" + str(bc))
                return 
        else:
            if a[i] == 1:
                ac += 1
            if b[i] == 1:
                bc += 1
            if abs(ac - bc) >= 1:
                print(i+1)
                print(str(ac) + ":" + str(bc))
                return
    print(str(ac) + ":" + str(bc))
    return 


a = li()
b = li()
main(a, b)  
