# auther yeling
from typing import List
import math

class Solution:
    def begin(self, n: int, nums :List[int]) :
        res = min(nums)
        if nums[0] == res :
            print("Yes")
        else :
            print("No")

sol = Solution()

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    allnums = (input()).split(' ')
    nums = []
    for t in allnums:
        nums.append(int(t))
    sol.begin(n, nums)
   
