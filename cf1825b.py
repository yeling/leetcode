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

def main(n, m, nums):
    nums.sort()
    ans = 0
    a,b,c = nums[0], nums[-1],nums[-2]
    ans = max(ans,b * n * ( m - 1) + c * (n - 1) * m  - (m*n -1) *a - (m - 1)*(n - 1)*min(b,c))

    a,b,c = nums[0], nums[-2],nums[-1]
    ans = max(ans,b * n * ( m - 1) + c * (n - 1) * m  - (m*n -1) *a - (m - 1)*(n - 1)*min(b,c))
    

    a,b,c = nums[-1], nums[0],nums[1]
    ans = max(ans,(m*n - 1)*a - b * n * ( m - 1) - c * (n - 1) * m +  (m - 1)*(n - 1)*max(b,c))

    a,b,c = nums[-1], nums[1],nums[0]
    ans = max(ans,(m*n - 1)*a - b * n * ( m - 1) - c * (n - 1) * m +  (m - 1)*(n - 1)*max(b,c))

    print(ans)

    return 

# nums = [1,3,1,4]
# main(2,2,nums)
caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    nums = li()
    main(n, m, nums)
   
