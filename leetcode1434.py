
# auther yeling
from typing import List
from bisect import *
from collections import *
import datetime
import math


class Solution:
    # TLE 46 / 65
    def numberWays2(self, hats: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        dp = defaultdict(int)
        start = '0'*41
        # print(start)
        dp[start] = 1
        for v in hats:
            next = defaultdict(int)
            for id in v:
                for key in list(dp.keys()):
                    if key[id] == '0':
                        # temp = key
                        value = dp[key]
                        temp = key[:id] + '1' + key[id+1:]
                        next[temp] = (next[temp] + value) % mod
            dp = next
            # print(v)
            # print(dp)
        sum = 0
        for k in dp:
            sum = (sum + dp[k]) % mod

        return sum % mod
    # TLE 52 / 65

    def numberWays3(self, hats: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        dp = defaultdict(int)
        start = 1 << 40
        # print(start)
        dp[start] = 1
        next = defaultdict(int)
        for v in hats:
            next = defaultdict(int)
            for id in v:
                dst = 1 << (id - 1)
                for key in list(dp.keys()):
                    if key & dst == 0:
                        # temp = key
                        value = dp[key]
                        temp = key | dst
                        next[temp] = (next[temp] + value) % mod
            dp = next
            print(len(dp))
            # print(dp)
        sum = 0
        for k in dp:
            sum = (sum + dp[k]) % mod

        return sum % mod

    # dp帽子找人
    def numberWays(self, hats: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        hatToPerson = defaultdict(list)
        maxHat = 0
        for i in range(len(hats)):
            for id in hats[i]:
                hatToPerson[id].append(i)
                maxHat = max(maxHat, id)
        # print(hatToPerson)
        n = len(hats)
        mask = 1 << n
        # dp[i][mask] i个帽子 mask当前有帽子的人
        dp = [[0] * mask for _ in range(maxHat + 1)]
        # print(dp)
        dp[0][0] = 1
        for i in range(1, maxHat + 1):
            for mask in range(1 << n):
                dp[i][mask] += dp[i - 1][mask]
                for j in hatToPerson[i]:
                    if mask & (1 << j):
                        dp[i][mask] += dp[i-1][mask ^ (1 << j)]
                    dp[i][mask] %= mod

        return dp[maxHat][(1 << n) - 1]


sol = Solution()
hats = [[3, 5, 1], [3, 5]]
# hats = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
hats = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# hats = [[3,4],[4,5],[5]]
# hats = [[1,2,4,6,7,8,9,11,12,13,14,15,16,18,19,20,23,24,25],[2,5,16],[1,4,5,6,7,8,9,12,15,16,17,19,21,22,24,25],[1,3,6,8,11,12,13,16,17,19,20,22,24,25],[11,12,14,16,18,24],[2,3,4,5,7,8,13,14,15,17,18,21,24],[1,2,6,7,10,11,13,14,16,18,19,21,23],[1,3,6,7,8,9,10,11,12,14,15,16,18,20,21,22,23,24,25],[2,3,4,6,7,10,12,14,15,16,17,21,22,23,24,25]]
starttime = datetime.datetime.now()
# print(sol.numberWays3(hats))
print(sol.numberWays(hats))

endtime = datetime.datetime.now()
print(endtime - starttime)
