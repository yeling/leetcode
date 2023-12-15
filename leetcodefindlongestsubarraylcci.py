
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
    # TLE 24 / 45 个通过的测试用例
    def findLongestSubarray2(self, array: List[str]) -> List[str]:
        n = len(array)
        ncnt = [0] * (n + 1)
        acnt = [0] * (n + 1)
        
        for i,v in enumerate(array):
            ncnt[i + 1] = ncnt[i]
            acnt[i + 1] = acnt[i]
            if v.isdigit():
                ncnt[i + 1] += 1
            else:
                acnt[i + 1] += 1
        left = -1
        maxlen = 0
        print(acnt)
        print(ncnt)
        diff = [i - j for i,j in zip(acnt,ncnt)]
        print(diff)

        for i in range(n):
            for j in range(i+1,n):
                tempn = ncnt[j+1] - ncnt[i]
                tempa = acnt[j+1] - acnt[i]
                if tempn == tempa and tempa + tempn > maxlen:
                    maxlen = tempa + tempn
                    left = i
        # print(left, maxlen)
        if left == -1:
            return []
        else:
            return array[left:left + maxlen]
        return
    #差分数组
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        n = len(array)
        ncnt = [0] * (n + 1)
        acnt = [0] * (n + 1)
        
        for i,v in enumerate(array):
            ncnt[i + 1] = ncnt[i]
            acnt[i + 1] = acnt[i]
            if v.isdigit():
                ncnt[i + 1] += 1
            else:
                acnt[i + 1] += 1
        print(acnt)
        print(ncnt)
        diff = [i - j for i,j in zip(acnt,ncnt)]
        print(diff)
        maxPos = defaultdict(int)
        for i,v in enumerate(diff):
            maxPos[v] = i

        maxlen = 0
        left = -1
        print(maxPos)
        for i,v in enumerate(diff):
            tempLen = maxPos[v] - i
            if tempLen > maxlen:
                left = i
                maxlen = tempLen

        # print(left, maxlen)
        if left == -1:
            return []
        else:
            return array[left:left + maxlen]
        return
    
# array = ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
# array = ["A","A","A","2"]
# print(len(array))
array = ["42","10","O","t","y","p","g","B","96","H","5","v","P","52","25","96","b","L","Y","z","d","52","3","v","71","J","A","0","v","51","E","k","H","96","21","W","59","I","V","s","59","w","X","33","29","H","32","51","f","i","58","56","66","90","F","10","93","53","85","28","78","d","67","81","T","K","S","l","L","Z","j","5","R","b","44","R","h","B","30","63","z","75","60","m","61","a","5","S","Z","D","2","A","W","k","84","44","96","96","y","M"]
sol = Solution()
ans = sol.findLongestSubarray(array)
print(len(ans), ans)

# ans1 = ["52","3","v","71","J","A","0","v","51","E","k","H","96","21","W","59","I","V","s","59","w","X","33","29","H","32","51","f","i","58","56","66","90","F","10","93","53","85","28","78","d","67","81","T","K","S","l","L","Z","j","5","R","b","44","R","h","B","30","63","z","75","60","m","61","a","5"]
# print(len(ans1))

