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
    res = []
    if n % 2 == 1:
        res = [2] * n
    else:
        res = [2] * (n - 2)
        res.append(1)
        res.append(3)
    print(*res)

        

   
