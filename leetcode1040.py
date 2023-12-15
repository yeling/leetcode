
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

class Solution:
    # AC
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        ans = [INF,0]
        #max
        for i in range(1,n):
            ans[1] += stones[i] - stones[i-1] - 1
        #去除两边，前面有两个，或者后面有两个，可以滚动，占用中间所有空格
        diff = min(stones[1] - stones[0], stones[-1] - stones[-2])
        if diff > 0:
            ans[1] = ans[1] - (diff - 1)

        #min l,r 还空余的位置填满
        for i,v in enumerate(stones):
            if v + n - 1 <= stones[-1]:
                dst = bisect_left(stones, v + n)  
                temp = n - dst + i
                #第一个空间大于2的情况,最后两个挨着需要特判
                #最后两个空间大于2的情况，前面两个挨着需要特判
                if temp == 1:
                    if stones[1] - stones[0] > 2 and stones[-1] - stones[-2] == 1: 
                        temp += 1
                    elif stones[-1] - stones[-2] > 2 and stones[1] - stones[0] == 1: 
                        temp += 1
                

                ans[0] =min(ans[0], temp)
                # print(i, temp)
        if ans[0] == INF:
            ans[0] = 0 
        return ans
    
nums = [6,4,9]
nums = [100,101,104,102,103]
nums = [3,8,10,12]
nums = [6,5,4,3,10]
sol = Solution()
print(sol.numMovesStonesII(nums))
