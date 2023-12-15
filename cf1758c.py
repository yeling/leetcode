# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

def main1():
    caseNum = int(input())
    for i in range(0, caseNum):
        n,x = [int(v) for v in input().split(' ')]
        res = []
        if n % x != 0:
            print(-1)
            continue
        elif n == x:
            res = list(range(1,n+1))
            res[n - 1] = 1
            res[0] = n
        else:
            res = list(range(1,n+1))
            res[n - 1] = 1
            res[0] = x
            pos = []
            temp = x
            m = 1
            while temp ** m < n:
                if n%(temp ** m) == 0:
                    pos.append(temp ** m)
                m += 1
            pos.append(n)
            for i in range(0,len(pos) - 1):
                res[pos[i] - 1] = pos[i + 1]
            # print('pos',pos)
        print(*res)

def main():
    caseNum = int(input())
    for i in range(0, caseNum):
        n,x = [int(v) for v in input().split(' ')]
        res = []
        if n % x != 0:
            print(-1)
            continue
        elif n == x:
            res = list(range(1,n+1))
            res[n - 1] = 1
            res[0] = n
        else:
            res = list(range(1,n+1))
            res[n - 1] = 1
            res[0] = x
            pos = []
            j = x
            p = 2 * x
            

            
            
            # print('pos',pos)
        print(*res)
        
main()
