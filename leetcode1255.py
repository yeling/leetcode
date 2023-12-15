
# auther yeling
from typing import List
from bisect import *

MOD = 10 ** 9 + 7


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        lett = [0] * 26
        for v in letters:
            lett[ord(v) - 97] += 1
        m = len(words)
        sum = 0
        for mask in range(1, 1 << m):
            curr = [0] * 26
            for i in range(m):
                if mask & (1 << i):
                    for v in words[i]:
                        curr[ord(v) - 97] += 1
            if all(x <= y for x, y in zip(curr, lett)):
                newScore = 0
                for x, y in zip(curr, score):
                    newScore += x*y
                sum = max(sum,newScore)
        return sum


words = ["dog", "cat", "dad", "good"]
letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0,
         0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sol = Solution()
print(sol.maxScoreWords(words, letters, score))
