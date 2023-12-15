# auther yeling
from typing import List
from bisect import *
from collections import *

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = [int(v) for v in input().split(' ')]
    l , r = 0, 0
    vally = 0
    n = len(nums)
    while r < n:
        find = True
        #c3
        if l == 0 or nums[l-1] > nums[l]:
            if r == n - 1 or nums[r] < nums[r+1]:
                vally += 1
                l = r = r + 1
            elif nums[r] == nums[r+1]:
                r = r + 1
            else:
                l = r = r + 1   
        else:
            l = r = r + 1
        if vally > 1:
            break
    if vally == 1:
        print('Yes')
    else :
        print('No')
   
