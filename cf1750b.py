# auther yeling
from typing import Sequence

# TLE
def begin(n: int, nums : Sequence):
    # print(one, zero)
    maxNum = 0
    currOne = 0
    currZero = 0
    one = 0
    zero = 0
    for i in range(len(nums)) :
        if nums[i] == '0':
            zero += 1
            currOne = 0
            currZero += 1
            maxNum = max(maxNum, currZero)
        else:
            one += 1
            currZero = 0
            currOne += 1
            maxNum = max(maxNum, currOne)

    res = max(one * zero, maxNum * maxNum)
    print(res)
    # return res


caseNum = int(input())
allnums = []
for i in range(0, caseNum):
    n = int(input())
    allnums.append(input())

for cheeses in allnums:
    begin(n, cheeses)

# result = [begin(n, cheeses) for cheeses in allnums]
# for item in result:
#     print(item)
    
