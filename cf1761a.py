# auther yeling
from typing import List
import math

class Solution:
    def begin(self, n: int, nums :List[int]) :
        # print(n , nums)
        n, a , b = nums
        if n == a and a == b:
            print('Yes')
        elif n - a - b > 1:
            print('Yes')
        else:
            print('No') 

sol = Solution()


caseNum = int(input())
for i in range(0, caseNum):
    allnums = (input()).split(' ')
    nums = []
    for t in allnums:
        nums.append(int(t))
    sol.begin(i, nums)
   
