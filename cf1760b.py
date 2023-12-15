# auther yeling
from typing import List
from bisect import *
from collections import *


caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    alpha = [0] * 26
    for v in s:
        alpha[ord(v) - 97] = 1
    res = 1
    for i,v in enumerate(alpha):
        if v == 1:
            res = i + 1
    print(res)
    

    
   
