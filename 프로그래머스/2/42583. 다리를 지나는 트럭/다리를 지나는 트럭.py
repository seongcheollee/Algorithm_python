from collections import deque


def solution(bridge_length, weight, truck_weights):
    
    # 대기 트럭
    q = deque(truck_weights)
    # 건너는 중인 트럭
    cross = deque([0] * bridge_length)
    time = 0
    temp = 0
    # 현재 감당가능한 무게
    while cross:
        time += 1
        n = cross.popleft()
        
        if n > 0:
            temp -= n
        
        # 1. 다리에 진입이 가능한가?
        if q:
            if weight >= q[0] + temp:
                temp += q[0]
                cross.append(q.popleft())
            else:
                cross.append(0)
        else:
            time += bridge_length -1
            break     


    return time

