# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue


caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    i = 0
    k = 1
    res = 'Yes'
    while i < n:
        if k % 2 != 0:
            i += 1
        elif k % 2 == 0:
            if i + 1 == n or s[i] != s[i + 1]:
                res = 'No'
                break
            i += 2
        k += 1
    print(res)



   
