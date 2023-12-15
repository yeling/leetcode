# auther yeling
from typing import List
from bisect import *
from collections import *


caseNum = int(input())
for i in range(0, caseNum):
    allnums = [int(v) for v in (input()).split(' ')]
    allnums.sort()
    print(allnums[1])

    
   
