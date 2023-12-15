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


def main(nums):
    # print(nums)
    n,a,b,c,d = nums
    if abs(b - c) > 1:
        print('No')
        return 
    if (b == 0 and c == 0) and (a > 0 and d > 0):
        print('No')
        return   
    if a + b + c + d != n - 1:
        print('No')
        return 
    

    print('Yes')
    
def check(s):
    n, a, b, c, d = 0,0,0,0,0
    n = len(s)
    pre = s[0]
    for i in range(1,n):
        if pre == 'x':
            if s[i] == 'x':
                a += 1
            else:
                b += 1
        elif pre == 'y':
            if s[i] == 'x':
                c += 1
            else:
                d += 1
        pre = s[i]
    print(n, a, b, c, d)
    return [n,a,b,c,d]


# s = 'xyyxyxxyxyxyyyxxxx'
# nums = check(s)
# main(nums)

# nums = [5, 1, 2, 1, 0]
# main(nums)

nums = li()
main(nums)

