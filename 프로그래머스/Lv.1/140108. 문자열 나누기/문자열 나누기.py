def solution(s):
    res = 0

    x = ''
    temp = ''
    
    x_c = 0
    x_nc = 0
    
    for n in s:
        # x 삽입
        if not x:
            x = n
            temp = n
            x_c += 1
            continue
        
        # x랑 같은지 카운트
        if x == n:
            x_c += 1
        else:
            x_nc += 1
        
        # 현재까지 읽은 문자열
        temp += n 
        
        # 카운트 비교
        if x_c == x_nc:
            print(temp)
            res += 1
            # 기준 문자열, 현재까지 읽은 문자열 초기화
            x = ''
            temp= ''
    
    # 나머지 문자열 존재 체크
    if temp:
        res+= 1
        


    return res