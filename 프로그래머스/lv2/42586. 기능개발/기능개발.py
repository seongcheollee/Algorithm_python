import math

def solution2(progresses, speeds):
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

# 문제 : 뭐해서 뭐해서 뭐하는 문제 

# progresses(작업진도)라는 리스트가 주어지고, 작업진도 < 100
# 리스트 대열만큼의 speed(작업속도)가 주어진다. 작업속도 =< 100
# 배포는 하루에 한 번, 작업이 100이 될 때 배포.
# 하지만 맨 앞이 진도100이 pop 되어야 그 뒤에도 진도100 pop 가능 
# ex) 진도=[92,94] 속도=[2,2]면 진도의 [92]가 100되어야 다음 날에 [94]도 나갈 수 있음
# 인덱스 기준 작업진도[0]값이 100되면 바로 뒷쪽 진도 100으로 준비된 애가 같이 나감

def solution(progresses, speeds):
    
    answer = []
    # 작업진도 리스트가 없어 질 때까지
    
    while progresses:
        # 몇개가 배포되는지
        cnt = 0
        # 진도 and 진도 맨앞이 100인 경우
        while progresses and progresses[0] >= 100:
            # 배포 카운트
            cnt +=1
            # 맨앞이 작업진도 100 일 때 그 작업과 속도를 제거
            progresses.pop(0)
            speeds.pop(0)
            
            # 진도 + 속도 반복
        progresses = [progresses[i] + speeds[i] for i in
                     range(len(progresses))]
        
        # 배포되면 카운트추가
        if cnt:
            answer.append(cnt)
            
    return answer

