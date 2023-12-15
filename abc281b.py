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


def main(s : str):
    n = len(s)
    if n != 8:
        print(NO)
        return
    if s[0].isupper() and s[7].isupper() and s[1:7].isdigit():
        temp = int(s[1:7])
        if 100000 <= temp <= 999999:
            print(YES)
            return
    print(NO) 
    


s = input()
# s = 'Q100000Z'
main(s)

