
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
    def lengthOfLIS(self, nums: List[int]) -> int:
        #1.贪心 + 二分
        #2.记录长度为N的序列，最小的数字
        # 我悟了！对于二分方法，“遍历给定的数组 nums，对于每个元素 i，找到d中第一个大于等于 i 的位置 it。如果it存在，要用i替换it。“
        # 原因有两点，
        # 一是，此时用i替换it，并不影响当前最长增长子序列的实际长度。其实无论怎么替换当前d[]中的存在元素都不影响当前最长子序列的实际长度（只有另一种情况时，往末尾增加新元素才会改变）。
        # 二是，之所以用i替换it，是为了得到一种“增益”，使得当前最长增长子序列序列增长的更慢一点。这是关键所在。
        cache = []
        for v in nums:
            index = bisect_left(cache,v)
            if index == len(cache):
                cache.append(v)
            elif v < cache[index]:
                cache[index] = v
            print(cache)
        return len(cache)
    
# nums = [10,9,2,5,3,7,101,18]
# nums = [0,1,0,4,5,2]
nums = [10, 19, 7 ,1, 17, 11, 8, 5 ,12, 9, 4, 18, 14 ,2 ,6, 15, 3 ,16, 13]
# nums = [6, 4, 3, 5, 2, 1]
sol = Solution()
print(sol.lengthOfLIS(nums))
