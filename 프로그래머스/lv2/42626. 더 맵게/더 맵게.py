import heapq

def solution(scoville, K):

    heapq.heapify(scoville)
    cnt = 0
    
    while scoville[0] < K:
        # 힙에서 팝한 값을
        # 섞은 음식의 스코빌 지수 적용해서 힙에 다시 넣기
        temp = heapq.heappop((scoville)) + (heapq.heappop((scoville)) * 2)
        
        heapq.heappush(scoville, temp)
        
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        cnt +=1 

    
    return cnt

