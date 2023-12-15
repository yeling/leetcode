
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    # AC
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        keys = arr2[:]
        #当前值为i时的最小操作次数
        dp = defaultdict(int)
        ans = INF
        for i in range(0, len(arr1)):
            if i == 0:
                for v in arr2:
                    dp[v] = 1
                dp[arr1[i]] = 0
            else:
                if arr1[i] not in dp:
                    dp[arr1[i]] = INF
                keys = list(dp.keys())
                keys.sort()
                
                curr = dp[keys[0]]
                next = defaultdict(int)
                ans = INF
                
                for j in range(1,len(keys)):
                    if keys[j] == arr1[i - 1] and keys[j] not in arr2:
                        curr = min(curr, dp[keys[j]])
                        ans = min(ans,curr)
                        continue
                    if keys[j] == arr1[i]:
                        next[keys[j]] = curr
                    else:
                        next[keys[j]] = curr + 1
                    curr = min(curr, dp[keys[j]])
                    ans = min(ans,next[keys[j]])
                if ans == INF:
                    return -1
            
                # print(arr1[i], dp, next, ans)
                dp = next
        if ans == INF:
            ans = -1

        return ans

    
arr1 = [1,5,3,6,7]
arr2 = [4,3,1]
arr1 = [1,5,3,6,7]
arr2 = [1,3,2,4]
arr1 = [1,5,3,6,7]
arr2 = [1,3,3,6]
arr1 = [0,11,6,1,4,3]
arr2 = [0,1,4,5,10,11]


sol = Solution()
print(sol.makeArrayIncreasing(arr1, arr2))
