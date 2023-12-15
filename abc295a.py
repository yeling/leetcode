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
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())


dst =  ['and', 'not', 'that', 'the' , 'you']
def main(n, s):
    for v in s:
        if v in dst:
            print('Yes')
            return
    print('No')


n = int(input())
words = input().split(' ')
main(n, words)

