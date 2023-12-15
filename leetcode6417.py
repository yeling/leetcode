
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

class FrequencyTracker:

    def __init__(self):
        self.cache = defaultdict(int)
        self.freq = defaultdict(int)
        return

    def add(self, number: int) -> None:
        if self.cache[number] != 0:
            self.freq[self.cache[number]] -= 1
        self.freq[self.cache[number] + 1] += 1
        self.cache[number] += 1
        return

    def deleteOne(self, number: int) -> None:
        if number in self.cache:
            self.freq[self.cache[number]] -= 1
            if self.cache[number] == 1:
                del self.cache[number]
            else:
                self.freq[self.cache[number] - 1] += 1
                self.cache[number] -= 1
        return

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0

