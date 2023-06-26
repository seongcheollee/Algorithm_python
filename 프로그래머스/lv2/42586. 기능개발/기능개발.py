from collections import deque
import math

def solution(progresses, speeds):
    res = []
    temp = []
    for i in range(len(progresses)):
        temp.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    first = 0
    for i in range(1, len(progresses)):
        if temp[first] < temp[i]:
            res.append(i - first)
            first = i

    res.append(len(progresses) - first)
            
    return res


