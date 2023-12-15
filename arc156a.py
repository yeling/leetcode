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

def main(n, s):
    one = s.count('1')
    if one == 2:
        if len(s) == 3:
            if s == '101':
                print('1')
                return
            else:
                print('-1')
        else:
            for i  in range(1,len(s)):
                if s[i] == '1' and s[i-1] == '1':
                    if i == 2 and len(s) == 4:
                        print('3')
                    else:
                        print('2')
                    return 
            print(1)
    elif one%2 == 0:
        print(one//2)
    else:
        print(-1)
    return 
# n = 0
# s = '01100'
# main(n, s)
caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    main(n, s)
   
