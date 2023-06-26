import math

def solution(progresses, speeds):
    res = []
    temp = []
    # 각각의 작업이 100을 넘는 값 추출
    for i in range(len(progresses)):
        temp.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    # 가장 선두의 작업이 걸리는 일수보다 작은 것들 count
    first = 0
    cnt = 1
    for i in range(1, len(progresses)):
        if temp[first] >= temp[i]:
            cnt += 1
        else:
            first = i
            res.append(cnt)
            cnt = 1

    # 마지막 작업 추가
    res.append(cnt)
            
    return res


