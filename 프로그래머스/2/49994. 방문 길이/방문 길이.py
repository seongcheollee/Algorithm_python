# 중복제외 경로 길이 탐색 문제
# 0,0 -> 5,5에서 시작
from collections import deque


def solution(dirs):
    answer = 0
    cnt = 0
    q = deque(dirs)
    x,y =4,4
    nx,ny = 0,0
    v = []
    
    while q:
        n = q.popleft()
        if n == "U":
            nx = x
            ny = y - 1
        elif n == "D":
            nx = x
            ny = y + 1
        elif n == "R":
            nx = x + 1
            ny = y
        else:
            nx = x -1
            ny = y
                
        if (0<=nx<10) and (0<=ny<10):
            if [nx, ny] not in v: 
                cnt += 1
                v.append([nx,ny])
        
            x = nx
            y = ny

    return cnt + 1
