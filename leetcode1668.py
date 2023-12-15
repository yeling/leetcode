
# auther yeling
from typing import List
import math
# 92 / 100 
class Solution:
    def maxRepeating2(self, sequence: str, word: str) -> int:
        maxSum = k = 0
        for i in range(len(sequence)):
            index = i
            k = 0
            while sequence[index:index+len(word)] == word:
                index += len(word)
                k = k + 1
            maxSum = max(maxSum, k)
            # print(maxSum, k)
        return maxSum
    def maxRepeating(self, sequence: str, word: str) -> int:
        maxSum = 0
        for i in range(1, len(sequence)//len(word) + 1):
            if word * i in sequence:
                maxSum += 1
        return maxSum

sol = Solution()

sequence = "ababc"
word = "ab"
# print(word * 10)
print(sol.maxRepeating(sequence,word))
