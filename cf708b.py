
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

def main(nums):
    a,b,c,d = nums
    # print(a,b,c,d)
    if sum(nums) == 0:
        print(0)
        return 
    cnt0 = (int)((sqrt(8*a + 1) + 1)//2)
    if (cnt0 * 2 - 1) * (cnt0 * 2 - 1) != 8*a + 1:
        print('Impossible')
        return
    
    cnt1 = (int)((sqrt(8*d + 1) + 1)//2)
    if (cnt1 * 2 - 1) * (cnt1 * 2 - 1) != 8*d + 1:
        print('Impossible')
        return
    if b == 0 and c == 0:
        if a > 0 and d > 0:
            print('Impossible')
        elif d > 0:
            print(''.join(['1' for v in range(cnt1)]))
        else:
            print(''.join(['0' for v in range(cnt0)]))
        return

    if b + c != cnt0 * cnt1:
        print('Impossible')
        return
    ret = [1] * cnt1
    if b%cnt1 != 0:
        ret.insert(-b%cnt1,0)

    ret = [0] * (b//cnt1) + ret
    if cnt0 > b//cnt1:
        after = cnt0 - b//cnt1
        if b%cnt1 != 0:
            after -= 1
        ret += [0]*after
                      
    # print(ret)
    retStr = "".join([str(v) for v in ret])
    print(retStr)

    return

def check(s):
    n = len(s)
    pre1, pre0 = [0] * (n + 1),[0] * (n + 1)
    
    for i,v in enumerate(s):
        pre1[i + 1] = pre1[i]
        pre0[i + 1] = pre0[i]
        if v == '0':
            pre0[i + 1] += 1
        else:
            pre1[i + 1] += 1
    b = 0 #01
    c = 0 #10
    for i,v in enumerate(s):
        if v == '0':
            b += pre1[n] - pre1[i+1]
            c += pre1[i+1]
        # print(i,v, b, c)
    a = pre0[n] * (pre0[n] - 1)//2
    d = pre1[n] * (pre1[n] - 1)//2
    return [a,b,c,d]


# s = '0101000100'
# nums = check(s)
# print(nums)
# main(nums)


nums = [1,2,3,4]
nums = [999961560, 0, 0, 999961560]
main(nums)
nums = li()
main(nums)
