
# auther yeling
from typing import List
import math
from functools import lru_cache

class Solution:
    # TLE 59 / 111 
    def splitArraySameAverage2(self, nums: List[int]) -> bool:
        all = sum(nums)
        if all & 1 != 0:
            return False
        
        return self.dfs(nums, 0, all, 0, 0)
    
    def dfs(self, nums, index, all, preSum, count):
        if index == len(nums):
            return False
        if preSum != 0 and preSum * len(nums) == all * count:
            return True
        ret = False
        #do nothing
        ret = self.dfs(nums, index + 1, all, preSum, count)
        #select
        ret |= self.dfs(nums, index + 1, all, preSum + nums[index], count + 1)
        return ret

    # 59 / 111 TLE
    def splitArraySameAverage3(self, nums: List[int]) -> bool:
        all = sum(nums)
        nums.sort()
        ave = all /len(nums)
        numA = [i for i in nums if i < ave]
        numB = [i for i in nums if i > ave]
        print(nums, numA, numB)
        return self.dfsA(numA, numB, 0, 0, 0, 0, all, len(nums))
    
    def dfsA(self, numA, numB, indexA, indexB, preSum, count, all, allCount):
        # print('dfsA', indexA, indexB, preSum, count)
        if count != allCount and preSum != 0 and preSum * allCount == all * count:
            return True
        if indexA == len(numA):
            return False

        ret = False
        #do nothing
        ret = self.dfsA(numA, numB, indexA + 1, indexB, preSum, count, all, allCount)
        #select
        if (preSum + numA[indexA]) * allCount > all * (count + 1):
            ret |= self.dfsA(numA, numB, indexA + 1, indexB, preSum + numA[indexA], count + 1, all, allCount)
        else:
            ret |= self.dfsB(numA, numB, indexA + 1, indexB, preSum + numA[indexA], count + 1, all, allCount)
        
        return ret
    
    def dfsB(self, numA, numB, indexA, indexB , preSum, count, all, allCount):
        # print('dfsB', indexA, indexB, preSum, count)
        if count != allCount and preSum != 0 and preSum * allCount == all * count:
            return True
        if indexB == len(numB):
            return False
        ret = False
        #do nothing
        ret = self.dfsB(numA, numB, indexA, indexB + 1, preSum, count, all, allCount)
        #select
        if (preSum + numB[indexB]) * allCount > all * (count + 1):
            ret |= self.dfsA(numA, numB, indexA, indexB + 1, preSum + numB[indexB], count + 1, all, allCount)
        else:
            ret |= self.dfsB(numA, numB, indexA, indexB + 1, preSum + numB[indexB], count + 1, all, allCount)
            
        return ret
    
    def splitArraySameAverage4(self, nums: List[int]) -> bool:
        all = sum(nums)
        n = len(nums)
        if n == 1:
            return False
        nums = [item * n - all for item in nums]
        # print(nums, sum(nums)/n)
        m = n // 2
        numA = nums[:m]
        numB = nums[m:]
        # print(nums, numA, numB)
        
        def dfs(index, array, preSum, cache):
            if index == len(array):
                return
            #do nothing
            dfs(index + 1, array, preSum, cache)
            #select
            cache.add(preSum + array[index])
            dfs(index + 1, array, preSum + array[index], cache)

        cacheA = set()
        cacheB = set()
        dfs(0, numA, 0, cacheA)
        dfs(0, numB, 0, cacheB)
        # print(cacheA, cacheB)
        sumB = sum(numB)
        if 0 in cacheA or 0 in cacheB:
            return True
        for item in cacheA:
            if -item != sumB and -item in cacheB:
                return True

        return False
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
        s = sum(nums)
        for i in range(n):
            nums[i] = nums[i] * n - s
        m = n//2
        left = set()
        right = set()
        for i in range(1, 1 << m):
            tot = sum(x for j, x in enumerate(nums[:m]) if i >> j & 1)
            if tot == 0:
                return True
            left.add(tot)
        rsum = sum(nums[m:])
        for i in range (1, 1 << (n - m)):
            tol = sum(x for j,x in enumerate(nums[m:]) if i >>j & 1)
            if tol == 0 or rsum != tot and -tot in left:
                return True
        return False
    
sol = Solution()

# nums = [1,2,3,4,5,6,7,8]
nums = [1,5,3]
# nums = [4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5]
# nums = [6,8,18,3,1]
# nums = [5,3,11,19,2]

test = [item for item in enumerate(nums)]
print(test)

# print(sol.splitArraySameAverage(nums))
