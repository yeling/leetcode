# auther yeling
from typing import List
from collections import *
import math

class Solution:
    def begin(self, n: int, nums :List[int]) :
        # print(n , nums)
        # in,out
        cache = [(set(),set()) for _ in range(n+1)]

        for i in range(n):
            for j in range(n):
                if nums[i][j] == 1:
                    cache[j+1][0].add(i+1)
                    cache[i+1][1].add(j+1)
        res = [set() for _ in range(n+1)]
        index = 1
        while True:
            empty = []
            # print('cache',cache)
            for i in range(1,len(cache)):
                if len(cache[i][0]) == 0 and len(cache[i][1]) != 0:
                    empty.append((i,cache[i]))
            if len(empty) == 0:
                break
            # print('empty',empty)
            for item in empty:
                res[item[0]].add(index)
                for dst in item[1][1]:
                    cache[dst][0].remove(item[0])
                    res[dst].add(index)
                    #最后一个了，需要再加1
                    if len(cache[dst][0]) == 0 and len(cache[dst][1]) == 0:
                        index += 1
                        res[dst].add(index)
                item[1][1].clear()
                index += 1

        # print(res)
        for i in range(1,len(res)):
            print(len(res[i]), *res[i])
            # n = len(res[i])
            # print(n, ' '.join([str(v) for v in res[i]]))
        return 0

sol = Solution()

lis = [1,2,3]
tu = (1,2,3)
dic = defaultdict()
dic['a'] = 1
dic['b'] = 2
print(lis, *lis)
print(tu, *tu)
print(dic, *dic)


# caseNum = int(input())
# for i in range(0, caseNum):
#     n = int(input())
#     allnums = []
#     for j in range(n):
#          allnums.append([int(v) for v in (input())])
   
#     sol.begin(n, allnums)
   
