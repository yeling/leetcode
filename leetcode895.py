
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue


MOD = 10 ** 9 + 7

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.group[self.freq[val]].append(val)
        self.maxFreq = max(self.maxFreq, self.freq[val])

    def pop(self) -> int:
        val = self.group[self.maxFreq].pop()
        self.freq[val] -= 1
        if len(self.group[self.maxFreq]) == 0:
            self.maxFreq -= 1
        return val




# Your FreqStack object will be instantiated and called as such:

freqStack = FreqStack()
# freqStack.push (5)#堆栈为 [5]
# freqStack.push (7)#堆栈是 [5,7]
# freqStack.push (5)#堆栈是 [5,7,5]
# freqStack.push (7)#堆栈是 [5,7,5,7]
# freqStack.push (4)#堆栈是 [5,7,5,7,4]
# freqStack.push (5)#堆栈是 [5,7,5,7,4,5]
# freqStack.pop ()#返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,5,7,4]。
# freqStack.pop ()#返回 7 ，因为 5 和 7 出现频率最高，但7最接近顶部。堆栈变成 [5,7,5,4]。
# freqStack.pop ()#返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,4]。
# freqStack.pop ()#返回 4 ，因为 4, 5 和 7 出现频率最高，但 4 是最接近顶部的。堆栈变成 [5,7]。
# freqStack.pop ()
# freqStack.pop ()
freqStack.push(6)
freqStack.push(8)
freqStack.push(6)
freqStack.push(6)
freqStack.push(8)
freqStack.push(9)
freqStack.pop ()
freqStack.push(8)
freqStack.pop ()





