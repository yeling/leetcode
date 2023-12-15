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

def main(n, nums):
    flag = True
    ans = []
    last = nums[0]
    ans.append(last)
    for i in range(1, n):
        if nums[i]%last != 0:
            ans.append(nums[i])
            last = nums[i]
        else:
            if last%2 == 0:
                ans.append(nums[i] + 1)
                last = nums[i] + 1  
            else:
                if last == 1:
                    temp = last
                    while nums[i]%temp == 0:
                        temp += 1
                    ans[-1] = temp
                    ans.append(nums[i])
                    last = nums[i]    
                else:
                    ans.append(nums[i] + 1)
                    last = nums[i] + 1  
    print(*ans)

    return 

# nums = [2, 4, 3, 6]
# main(len(nums), nums)

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
