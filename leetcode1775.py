
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
    #1.大数减去，记录每个数的修改次数
    #2.小数增加，记录每个数的修改次数
    #3.获取每个数的累计修改次数，取最小值
    def minOperations2(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(nums1)
        s2 = sum(nums2)
        big, small = None, None
        bs, ss = 0, 0

        if s1 == s2:
            return 0
        elif s1 > s2:
            big, small, bs, ss = nums1, nums2, s1, s2
        else:
            big, small, bs, ss = nums2, nums1, s2, s1

        # print(big, small, bs, ss)
        dpBig = []
        dpSmall = []
        big.sort(reverse=True)
        small.sort()
        # print(big, small, bs, ss)
        #1.处理Big数组
        i, temp = 0, bs
        dpBig.append(temp)
        while temp >= ss and i < len(big):
            if big[i] != 1:
                temp -= big[i] - 1
                dpBig.append(temp)
            i += 1
        #2.处理Small数组
        i, temp = 0, ss
        dpSmall.append(temp)
        while temp <= bs and i < len(small):
            if small[i] != 6:
                temp += 6 - small[i]
                dpSmall.append(temp)
            i += 1
        # print(dpBig, dpSmall)
        if dpBig[-1] > dpSmall[-1]:
            return -1
        res = inf
        for i,v in enumerate(dpBig):
            index = bisect_left(dpSmall, v)
            if index == len(dpSmall):
                index = inf
            # print(v, index)
            res = min(res, index + i)
        return res

    #1.大数减去，记录每个数的修改次数
    #2.小数增加，记录每个数的修改次数
    #3.大数减去时，优先使用6贡献了-5，小数增加时，优先使用1，增加5
    #  6,1两者对结果的贡献时相同的，所以可以用 diff[6]来存储贡献，1，5的数字的个数
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(nums1)
        s2 = sum(nums2)
        big, small = None, None
        bs, ss = 0, 0
        if s1 == s2:
            return 0
        elif s1 > s2:
            big, small, bs, ss = nums1, nums2, s1, s2
        else:
            big, small, bs, ss = nums2, nums1, s2, s1
        
        diff = [0] * 6
        for v in big:
            diff[v - 1] += 1
        for v in small:
            diff[6 - v] += 1
        
        delta = bs - ss
        res = 0
        temp = 0
        print(diff, delta)
        for i in range(5,0,-1):
            if temp + i * diff[i] >= delta:
                return res + (delta - temp + i - 1)//i
            else:
                temp += i * diff[i]
                res += diff[i]
        return -1


nums1 = [1, 6, 3, 4, 5, 2]
nums2 = [1, 1, 2, 2, 2, 2]
nums1 = [5,2,1,5,2,2,2,2,4,3,3,5]
nums2 = [1,4,5,5,6,3,1,3,3]
# nums1 = [1,1,1,1,1,1,1]
# nums2 = [6]
# nums1 = [6,4]
# nums2 = [2]
nums1 = [6,6]
nums2 = [1]
sol = Solution()
print(sol.minOperations2(nums1, nums2))
print(sol.minOperations(nums1, nums2))
