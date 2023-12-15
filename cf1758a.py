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
    s = input()
    rev = ''
    for j in range(len(s) - 1, -1, -1):
        rev += s[j]
    print(s + rev)
   
