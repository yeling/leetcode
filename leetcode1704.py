
# auther yeling
from typing import List
import math
import string

class Solution:
    def halvesAreAlike2(self, s: str) -> bool:
        checkTable = ['a','e','i','o','u','A','E','I','O','U']
        one = {}
        two = {}
        half = len(s)//2
        for i in range(half):
            one.setdefault(s[i], 0)
            one[s[i]] += 1
            two.setdefault(s[i + half], 0)
            two[s[i + half]] += 1
        # print(one,two)
        suma = 0
        sumb = 0
        for item in checkTable:
            if item in one:
                suma += one[item]
            if item in two:
                sumb += two[item]
        return suma == sumb

    def halvesAreAlike3(self, s: str) -> bool:
        checkTable = ['a','e','i','o','u','A','E','I','O','U']
        one = {}
        two = {}
        for i in string.ascii_letters:
            one.setdefault(i, 0)
            two.setdefault(i, 0)

        half = len(s)//2
        for i in range(half):
            one[s[i]] += 1
            two[s[i + half]] += 1
        # print(one,two)
        suma = 0
        sumb = 0
        for item in checkTable:
            if item in one:
                suma += one[item]
            if item in two:
                sumb += two[item]
        return suma == sumb

    def halvesAreAlike(self, s: str) -> bool:
        checkTable = ['a','e','i','o','u','A','E','I','O','U']
        half = len(s)//2
        suma = 0
        sumb = 0
        half = len(s)//2
        for i in range(half):
            if s[i] in checkTable:
                suma += 1
            if s[i + half] in checkTable:
                sumb += 1
        return suma == sumb
        
    
sol = Solution()

s = "AbCdEfGh"
print(sol.halvesAreAlike(s))
