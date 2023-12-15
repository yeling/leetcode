
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue


MOD = 10 ** 9 + 7

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        #去除能沟通的好友，在不能沟通的中，教会最多人的那门语言
        # 所有不能沟通的人数 - 会最多语言的人数，
        all = defaultdict(int)
        allPeople = set()
        for v in friendships:
            fri = False
            for p in product(languages[v[0] - 1], languages[v[1]- 1]):
                # print(p)
                if p[0] == p[1]:
                    fri = True
                    break
            if fri == False:
                if v[0] not in allPeople:
                    allPeople.add(v[0])
                    for i in languages[v[0] - 1]:
                        all[i] += 1
                if v[1] not in allPeople:
                    allPeople.add(v[1])
                    for i in languages[v[1] - 1]:
                        all[i] += 1
        #所有不能沟通的人数 - 会最多语言的人数，
        print(all, allPeople)
        maxL = 0
        for k in all:
            if maxL < all[k]:
                maxL = all[k]
        res = len(allPeople) - maxL
        return res
    
n = 3
languages = [[2],[1,3],[1,2],[3]]
friendships = [[1,4],[1,2],[3,4],[2,3]]

sol = Solution()
print(sol.minimumTeachings(n,languages,friendships))
