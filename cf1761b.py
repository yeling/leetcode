# auther yeling
from typing import List
from collections import *
import math

class Solution:
    def begin2(self, n: int, nums :List[int]) :
        # print(n , nums)
        
        res = 0
        left = 0
        while left < len(nums) - 1 and len(nums) > 2:
            print(nums)
            if nums[left - 1] != nums[left + 1]:
                nums = nums[:left] + nums[left + 1:]
                res += 1
                if left > 0:
                    left -= 1
            else:
                left += 1
        if len(nums) <= 2:
            res += len(nums)
        else:
            res += (len(nums) - 2)//2 + 2
                
        print(res)
    #总是可以先干掉相同的元素 12123434 ,从连接的地方开始
    def begin(self, n: int, nums :List[int]) :
        c = Counter(nums)
        print(c, len(c))
        print(n//2 + 1 if len(c) == 2 else n)

        return

# nums = [1, 2, 3, 1, 2]


sol = Solution()
# nums = [1, 2, 3, 1, 2]
nums = [1, 2, 3, 2, 3, 2]
sol.begin(6, nums)

# caseNum = int(input())
# for i in range(0, caseNum):
#     n = int(input())
#     allnums = (input()).split(' ')
#     nums = []
#     for t in allnums:
#         nums.append(int(t))
#     sol.begin(n, nums)
   
