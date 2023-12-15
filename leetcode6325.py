
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
    # 240 / 1071 个通过测试用例
    # 413 / 1071 个通过测试用例
    # 686 / 1071
    # 947 / 1071
    # 1059 / 1071
    # AC

    def repairCars(self, ranks: List[int], cars: int) -> int:
        cnt = defaultdict(int)
        for v in ranks:
            cnt[v] += 1
        all = list(cnt.keys())
        all.sort()
        # print(all)
        left = 1
        right = (cars*cars//cnt[all[0]] + 1) * all[0]
        target = cars

        while left <= right:
            mid = left + (right - left)//2
            tempCars = 0
            for v in all:
                tempCars += int(sqrt(mid//v)) * cnt[v]   

            if target <= tempCars:
                right = mid - 1
            elif target > tempCars:
                left = mid + 1
            print(mid, tempCars, left, right)

        ans = left
        return ans

    
ranks = [5,1,8]
cars = 6
ranks = [4,2,3,1]
cars = 10
ranks = [3]
cars = 52
# ranks = [1,1,3,3]
# cars = 74
# ranks = [3,5,4,3]
# cars = 1

# ranks = [3,3,1,2,1,1,3,2,1]
# cars = 58

sol = Solution()
print(sol.repairCars(ranks, cars))

# print(sol.repairCars2(ranks, cars))
