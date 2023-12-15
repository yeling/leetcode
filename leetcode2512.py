
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
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        n = len(student_id) 
        cache = [0] * n
        pf = set(positive_feedback)
        nf = set(negative_feedback)
        for i in range(n):
            temp = report[i].split(' ')
            for v in temp:
                if v in pf:
                    cache[i] += 3
                elif v in nf:
                    cache[i] -= 1
        # print(cache)
        pa = list([-v,i] for v,i in zip(cache, student_id))
        pa.sort()
        ans = []
        for i in range(k):
            ans.append(pa[i][1])


        return ans
    
positive_feedback = ["smart","brilliant","studious"]
negative_feedback = ["not"]
report = ["this student is studious","the student is smart"]
student_id = [1,2]
k = 2
sol = Solution()
print(sol.topStudents(positive_feedback, negative_feedback, report, student_id, k))
