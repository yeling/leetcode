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

def digit(n):
    ans = 0
    while n > 0:
        ans += n%10
        n//=10
    return ans

def main(n):
    small = True
    a = 0
    b = 0
    add = 1
    src = n
    while n > 0:
        temp = n%10
        if temp%2 == 0:
            a += add * (temp - temp//2)
            b += add * (temp//2)
        else:
            if small and temp%2 != 0:
                a += add * (temp//2)
                b += add * (temp - temp//2)
            else:
                a += add * (temp - temp//2)
                b += add * (temp//2)
            small = not small
        n //= 10
        add *= 10

    print(a,b)
    # print(a,b, a + b == src, abs(digit(a) - digit(b)) <=1 )
    return 

# for i in range(10000):
#     main(i)

# main(9999)
caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    main(n)
   
