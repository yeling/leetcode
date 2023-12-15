
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
from heapq import *
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        #单调栈
        n = len(positions)
        pair = [[positions[i],healths[i], directions[i],i] for i in range(n)]
        pair.sort()
        print(pair)
        #存储向右的
        stack = []
        ans = []
        for i in range(n):
            if len(stack) == 0:
                if pair[i][2] == 'L':
                    ans.append(pair[i])
                else:
                    stack.append(pair[i])
            else:
                if pair[i][2] == 'R':
                    stack.append(pair[i])
                else:
                    while len(stack) > 0:
                        temp = stack.pop()
                        if temp[1] > pair[i][1]:
                            temp[1] -= 1
                            stack.append(temp)
                            pair[i][1] = 0
                            break
                        elif temp[1] == pair[i][1]:
                            pair[i][1] = 0
                            break
                        else:
                            pair[i][1] -= 1
                    if pair[i][1] > 0:
                        ans.append(pair[i])
        for v in stack:
            ans.append(v)
        ans.sort(key =lambda x:x[3])
        # print(ans)
        pans = [v[1] for v in ans]
        return pans
    
positions = [5,4,3,2,1]
healths = [2,17,9,15,10]
directions = "RRRRR"
positions = [3,5,2,6]
healths = [10,10,15,12]
directions = "RLRL"

positions = [2]
healths = [2]
directions = "L"

sol = Solution()
print(sol.survivedRobotsHealths(positions, healths, directions))
