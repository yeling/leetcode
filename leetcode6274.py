
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

class Skill(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
    
    def __lt__(self, other): 
        if self.priority == other.priority:
            return self.description < other.description
        else:
            return self.priority > other.priority
                   
    def __str__(self):
        return '(' + str(self.priority)+',\'' + self.description + '\')'
    
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:  
        score = defaultdict(int)
        pset = set(positive_feedback)
        nset = set(negative_feedback)

        for s in zip(report, student_id):
            words = s[0].split(' ')
            for p in words:
                if p in pset:
                    score[s[1]] += 3
                elif p in nset:
                    score[s[1]] -= 1
        all = PriorityQueue()
        for v in score:
            all.put(Skill(score[v],v))
        ans = []
        for _ in range(k):
            ans.append(all.get().description)
        return ans
    
positive_feedback = ["smart","brilliant","studious"]
negative_feedback = ["not"]
report = ["this student is studious","the student is smart"]
student_id = [1,2]
k = 2

positive_feedback = ["smart","brilliant","studious"]
negative_feedback = ["not"]
report = ["this student is not studious","the student is smart"]
student_id = [1,2]
k = 2

positive_feedback = ["fkeofjpc","qq","iio"]
negative_feedback = ["jdh","khj","eget","rjstbhe","yzyoatfyx","wlinrrgcm"]
report = ["rjstbhe eget kctxcoub urrmkhlmi yniqafy fkeofjpc iio yzyoatfyx khj iio","gpnhgabl qq qq fkeofjpc dflidshdb qq iio khj qq yzyoatfyx","tizpzhlbyb eget z rjstbhe iio jdh jdh iptxh qq rjstbhe","jtlghe wlinrrgcm jnkdbd k iio et rjstbhe iio qq jdh","yp fkeofjpc lkhypcebox rjstbhe ewwykishv egzhne jdh y qq qq","fu ql iio fkeofjpc jdh luspuy yzyoatfyx li qq v","wlinrrgcm iio qq omnc sgkt tzgev iio iio qq qq","d vhg qlj khj wlinrrgcm qq f jp zsmhkjokmb rjstbhe"]
student_id = [96537918,589204657,765963609,613766496,43871615,189209587,239084671,908938263]
k = 3

sol = Solution()
print(sol.topStudents(positive_feedback, negative_feedback, report, student_id, k))
