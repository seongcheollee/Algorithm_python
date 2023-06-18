def solution(citations):
    
    citations.sort()
    
    n = len(citations)
    
    # 중간 값 찾기
    # 0 1 3 5 6
    for i in range(n):
        if citations[i] >= n-i:
            return n-i
        
    return 0