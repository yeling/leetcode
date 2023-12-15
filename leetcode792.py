
# auther yeling
from typing import List
from bisect import *

class Solution:
    # TLE 41 / 53 
    def numMatchingSubseq2(self, s: str, words: List[str]) -> int:
        sum = 0
        for item in words:
            i,j = 0,0
            while i < len(s) and j < len(item):
                # print(i,j)
                if item[j] != s[i]:
                    i += 1
                else:
                    i += 1
                    j += 1
            if j == len(item):
                sum += 1
            # print(item, sum)
        return sum
    
    # TLE 52 / 53
    # AC 二分查找过了
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        sum = 0
        pos = [[] for _ in range(26)]
        
        for i,w in enumerate(s):
            pos[ord(w) - 97].append(i)
            
        # print(pos)
        for item in words:
            find = False
            lastPos = -1
            for iv in item:
                find = False
                newPos = bisect(pos[ord(iv) - 97], lastPos)
                # print(lastPos)
                if newPos != len(pos[ord(iv) - 97]):
                    lastPos = pos[ord(iv) - 97][newPos]
                    find = True
                if find == False:
                    break
            if find:
                sum += 1
            # print(item, sum)
        return sum

 
# s = "dsahjpjauf"
# words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]

s = "abcde"
words = ["acd","ace"]

sol = Solution()
# print(ord('a'))

nums = [i for i in range(10)]
print(nums)
print('insert pos ' ,bisect(nums,1))
print('insert pos ' ,bisect_left(nums,1))


print(sol.numMatchingSubseq2(s,words))
print(sol.numMatchingSubseq(s,words))
