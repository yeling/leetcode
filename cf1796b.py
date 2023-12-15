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
    maxlen = 0
    maxStr = ''

    for i in range(len(a)):
        for j in range(len(b)):
            k = 0
            while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
                k +=1
                if k > 1:
                    break
                
            if k > maxlen:
                maxlen = k 
                maxStr = a[i:i + k]
                if maxlen > 1:
                    break
        if maxlen > 1:
            break
        
    if maxlen > 1:
        print('Yes')
        print('*' + maxStr + '*')
    elif maxlen == 0:
        print('No')
    elif maxlen == 1:
        if a[0] == b[0]:
            print('Yes')
            print(a[0] + '*')
        elif a[-1] == b[-1]:
            print('Yes')
            print('*' + a[-1])
        else:
            print('No')

            


    return 

caseNum = int(input())
for i in range(0, caseNum):
    a = input()
    b = input()
    main(a,b)
   
