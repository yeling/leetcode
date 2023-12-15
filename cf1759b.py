# auther yeling
from typing import List
import math

class Solution:
    def begin(self, m: int, s: int, nums :List[int]) :
        # print(m , s, nums)
        # print(nums)
        nums.sort()
        ts = 0
        index = 1
        ni = 0
        while ts <= s:
            # print('ts ', ts, ni)
            if ni < len(nums) and index == nums[ni]:
                ni += 1
            else:
                ts += index
            if ts == s and ni == len(nums):
                print('Yes')
                return
            index += 1
        print('No')

sol = Solution()


caseNum = int(input())
for i in range(0, caseNum):
    first = (input()).split(' ')
    allnums = (input()).split(' ')
    nums = []
    for t in allnums:
        nums.append(int(t))
    sol.begin(int(first[0]), int(first[1]), nums)
   
