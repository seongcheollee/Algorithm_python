def solution(b, y):
    res = []
    # 사각형의 크기를 통해 나올 수 있는 가로 세로 변수 뽑기
    # (b+y) = 사각형의 총 넓이
    # 나올 수 있는 row, col을 약수 찾기
    # 제일 작은 사각형 3x3
    for i in range(3,((b+y)//2)+1):
        # i가 약수면
        if (b+y) % i == 0:
            # i = row , (b+y) // i = column
            if i >= (b+y) // i:
                res.append([i,(b+y)//i])
    print(res)
    # 모든 경우의 수 중 해당하는 것 찾기
    for sq in res:
        # 사각형 북 남, 사각형의 동 서 이미 포함시킨거 제거(북 남에 해당) 이 b의 개수면
        if sq[0] * 2 + (sq[1] - 2) * 2 == b:
            return [sq[0], sq[1]]
        
        
    
    
    return res