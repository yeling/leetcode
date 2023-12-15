# auther yeling
from typing import List
import math

class Solution:
    def begin(self, n: int, strs :List[int]) :
        for str in strs:
            dst = 'Yes'*(len(str)//3 + 2)
            if str in dst:
                print('Yes')
            else:
                print('No')
       

sol = Solution()


caseNum = int(input())
nums = []
for i in range(0, caseNum):
    allnums = input()
    nums.append(allnums)
sol.begin(i, nums)
   
