# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main(n, s):
    arr = s.split(' ')
    arr.sort(key = lambda x : (x[1],x[0]))
    print(*arr)
    #BCD
    return 


n = int(input())
s = input()
main(n, s)
