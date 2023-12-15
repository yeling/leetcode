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

    
#暴力模拟
def main(n, k, h, p):
    while True:
        minP = INF
        for i in range(n):
            if h[i] > 0:
                h[i] -= k
            if h[i] > 0:
                minP = min(minP, p[i])
        if minP == INF:
            print("Yes")
            return 
        else:
            k -= minP
            if k <= 0:
                print("No")
                return 
        print(h, k)
    return 

#暴力优化
def main3(n, k, h, p):
    minP = INF
    index = -1
    while True:
        #P最小值的为h为0时，P的最小值才会发生变化
        if index != -1:
            c = 0
            i = 0
            while c <= h[index] and k > i * minP:
                c += k - i * minP
                i += 1
            k = k - i*minP
            if k <= 0:
                print("No")
                return 
        else:
            c = k
        
        minP = INF
        index = -1 
        for i in range(n):
            if h[i] > 0:
                h[i] -= c
            if h[i] > 0:
                if minP > p[i]:
                    minP = p[i]
                    index = i
                elif minP == p[i] and h[i] < h[index]:
                    index = i
        if minP == INF:
            print("Yes")
            return 
        else:
            # k -= minP
            if k <= 0:
                print("No")
                return 

    return 


n = 6
k = 7
h = [18, 5, 13, 9, 10,1]
p = [2, 7, 2, 1, 2, 6]
# n = 4
# k = 7
# h = [1, 6, 10, 9]
# p = [5, 5, 3, 9]
n = 3
k = 4
h = [5, 5, 5]
p = [4, 4, 4]
# main(n,k,h,p)
# main3(n,k,h,p)


caseNum = int(input())
for i in range(0, caseNum):
    n,k  = li()
    h = li()
    p = li()
    # main(n,k,h,p)
    main3(n,k,h,p)
    
   
