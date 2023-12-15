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
    n,a,b = [int(v) for v in input().split(' ')]
    # print(n , a, b)
    if a > b:
        print(1)
    else:
        print((n - 1)//a + 1)


   
