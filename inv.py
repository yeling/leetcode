
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

#扩展欧几里得
def ExpGcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = ExpGcd(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y, q

def Inv( a,  n): 
    x, y, q = ExpGcd(a, n) 
    x = (x % n + n) % n
    return x

#逆元，费马小定理，快速幂版本，mod为素数
def Exp(a, n, mod):
    ans = 1
    while n != 0:
        if n & 1 != 0:
            ans = ans * a %mod
        a = a * a % mod
        n >>= 1
    return ans

def Inv2(a, p):
    return Exp(a, p-2, p)

a = 3
p = 11

print(Inv(a,p))
print(Inv2(a,p))