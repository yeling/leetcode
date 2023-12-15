
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
    # 57 / 59 TLE
    def smallestSubarrays2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        dst = [0] * (n + 1)
        
        for i in range(n):
            dst[n - 1 - i ] = dst[n - i] | nums[n - 1 - i] 
        cache = set(dst)
        #(value,start)
        curr = defaultdict(list)
        # curr[nums[0]].append(0)
        for i in range(n):
            next = defaultdict(list)
            for k in curr:
                ne = k|nums[i] 
                for v in curr[k]:
                    if dst[v] == ne:
                        ans[v] = i - v + 1
                    else:
                        next[ne].append(v)
                
            if nums[i] == dst[i]:
                ans[i] = 1
            else:
                next[nums[i]].append(i)
            curr = next
            
            
        return ans
    #TLE
    def smallestSubarrays3(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        dst = [0] * (n + 1)
        
        for i in range(n):
            dst[n - 1 - i ] = dst[n - i] | nums[n - 1 - i] 
        cache = set(dst[0:n])
        # print(cache)
        #(value,start)
        curr = set()
        # curr[nums[0]].append(0)
        cnt = 0
        need = defaultdict(list)
        for i in range(n):
            next = set()   
            print(curr, ans)
            for k in curr:
                ne = k|nums[i]
                if ne in need:
                    temp = []
                    for v in need[ne]:
                        if dst[v] == ne:
                            ans[v] = i - v + 1
                        else:
                            temp.append(v)
                    need[ne] = temp
                    if len(temp) > 0:
                        next.add(ne)
                        need[ne] = temp
                    else:
                        del need[ne]

                else:
                    next.add(ne)
                # next[ne] += curr[k][:]
            if nums[i] == dst[i]:
                ans[i] = 1
            else:
                next.add(nums[i])
                need[dst[i]].append(i)

            curr = next
        # print(cnt)
            
        return ans
    #AC
    def smallestSubarrays4(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i,v in enumerate(nums):
            ans[i] = 1
            for j in range(i-1,-1,-1):
                if (nums[j] | v) == nums[j]:
                    break
                nums[j] |= v
                ans[j] = i - j + 1

        return ans
    #03X
    def smallestSubarrays5(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ors = []  # 按位或的值 + 对应子数组的右端点的最小值
        for i in range(n - 1, -1, -1):
            print(ors)
            num = nums[i]
            ors.append([0, i])
            k = 0
            # 这里用到了数组原地修改
            for p in ors:
                p[0] |= num
                if ors[k][0] == p[0]:
                    ors[k][1] = p[1]  # 合并相同值，下标取最小的
                else:
                    k += 1
                    ors[k] = p
            del ors[k + 1:]
            # 本题只用到了 ors[0]，如果题目改成任意给定数值，可以在 ors 中查找
            ans[i] = ors[0][1] - i + 1
        return ans
    #03X + mine
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        curr = defaultdict(int) #存储右边所有按位或的结果，坐标尽可能的小
        for i in range(n - 1, -1, -1):
            next = defaultdict(int)
            for v in curr:
                temp = v | nums[i]
                next[temp] = curr[v] # 更新最小的节点
            next[nums[i]] = i
            ans[i] = next[max(next.keys())] - i + 1 # 按位或最大的值，最小坐标位为当前的结果
            curr = next
        return ans
    
# nums = [1,0,2,1,3]
# nums = [1,2]
nums = [4,0,5,6,3,2]
# nums = [0] * (10 ** 2)
# nums[-1] = 2
sol = Solution()
print(sol.smallestSubarrays2(nums))
print(sol.smallestSubarrays(nums))
