# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

def main1(n):
    res = []
    mlcm = n - 1
    for i in range(1, n//2 + 1):
        temp = i * (n - i) / gcd(i, n - i)
        if temp <= mlcm:
            mlcm = temp
            res = [i, n - i]
    print(*res, mlcm)

def main(n):
    if n % 2 == 0:
        print(n//2, n//2)
        return 
    dst = int(sqrt(n) + 1)
    dst = min(dst, n - 2)
    find = False
    for i in range(2,dst + 1):
        # print('hh',n,i)
        if n % i == 0:
            # print(n//i, n - n//i, n//i * (n - n//i)/ gcd(n - n//i,n//i ))
            print(n//i, n - n//i)
            find = True
            break
    if find == False:
        print(1, n-1)
        
caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    main(n)
    # main1(n)
        
