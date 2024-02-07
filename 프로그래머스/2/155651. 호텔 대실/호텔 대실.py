from heapq import heappop, heappush

def solution(book_time):
    rooms = []
    room_cnt = 0
    
    # # 10분 후 계산 했을 경우 분 단위가 59넘어가면 시간 증가해야 하고 분은 오버된 수치
    # for b in book_time:
    #     for i in range(2):
    #         if i == 1:
    #             b[i] = int(b[i].replace(":",""))+10                
    #         else:
    #             b[i] = int(b[i].replace(":",""))
    
    # 위 해결을 위해 분단위로 재구성
    for b in book_time:
        for i in range(2):
            if i == 1:
                b[i] = int(b[i].split(":")[0]) * 60 + int(b[i].split(":")[1]) + 10
            else:
                b[i] = int(b[i].split(":")[0]) * 60 + int(b[i].split(":")[1])
    
    # 입장 시간이 빠른 순으로 정렬            
    book_time.sort()

    
    for s, e in book_time:
        # 룸에 손님이 하나도 없으면
        if not rooms:
            heappush(rooms,e)
            room_cnt += 1
            continue
        # 가장 빨리 나가는 손님보다 다음 입실자가 같거나 늦게 들어오면
        if rooms[0] <= s:
            heappop(rooms)
        else:
            room_cnt += 1 # 그렇지 않은 경우 룸 개수 증가
        heappush(rooms,e)
    
    return room_cnt


