def solution(b, y):
    res = []
    # 사각형의 크기를 통해 나올 수 있는 가로 세로 변수 뽑기
    # (b+y) = 사각형의 총 넓이
    # 나올 수 있는 row, col을 약수 찾기
    for i in range(3,((b+y)//2)+1):
        # 약수면
        if (b+y) % i == 0:
            # 제일 작은 사각형 3x3
            # i = row , (b+y) // i = column
            if i >= 3 and (b+y)//i >= 3:
                if i >= (b+y) // i:
                    res.append([i,(b+y)//i])
    print(res)
    # 모든 경우의 수 중 해당하는 것 찾기
    for sq in res:
        if sq[0] * 2 + (sq[1] - 2) * 2 == b:
            return [sq[0], sq[1]]
        
        
    
    
    return res