# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main(n, nums):
    ans = 0
    for i in range(n):
        for j in range(i+2,n):
            temp = nums[i:j+1]
            temp.sort()
            # print(temp, sum(temp[-3:]))
            tempAns = sum(temp[-3:]) - (j - i)
            if tempAns > ans:
                ans = tempAns
            print(i, j , tempAns, ans)
    print(ans)
    return 
# main(5, [5,1,4,2,3])
caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
