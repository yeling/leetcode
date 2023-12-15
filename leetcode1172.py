
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class DinnerPlates:
    # 14 / 15 
    def __init__(self, capacity: int):
        #(index) 存储没有满的队列，队列为空，存储到最后一项
        self.stack = PriorityQueue()
        self.cache = []
        self.capacity = capacity

    def push(self, val: int) -> None:
        #
        flag = False
        while not self.stack.empty():
            first = self.stack.get()
            if len(self.cache[first]) < self.capacity:
                self.cache[first].append(val)
                flag = True
                if len(self.cache[first]) < self.capacity:
                    self.stack.put(first)
                break
        if flag == False:
            #最后一项
            if len(self.cache) > 0 and len(self.cache[-1]) < self.capacity:
                self.cache[-1].append(val)
            else:
                self.cache.append([val])  
        # flag = False
        # for v in self.cache:
        #     if len(v) < self.capacity:
        #         v.append(val)
        #         flag = True
        #         break
        # if flag == False:
        #     self.cache.append([val])    
        return


    def pop(self) -> int:
        ans = -1
        for i in range(len(self.cache) - 1, -1, -1):
            if len(self.cache[i]) > 0:
                ans = self.cache[i].pop()
                break
            if len(self.cache[i]) == 0:
                self.cache.pop(i)
        return ans

    def popAtStack(self, index: int) -> int:
        ans = -1
        if len(self.cache) > index and len(self.cache[index]) > 0:
            ans = self.cache[index].pop()
            #不是最后一项才存
            if index != len(self.cache) - 1:
                self.stack.put(index)
        return ans


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
    

# ca = []
# ca.append
# ca.pop
