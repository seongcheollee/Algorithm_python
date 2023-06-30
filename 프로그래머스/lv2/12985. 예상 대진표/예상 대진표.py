

def solution(n,a,b):

    # a 구간 , b 구간 찾기
    # 구간이 다르다면 b 구간 반환
    # 구간이 같다면 
    
    i = 0
    j = 0

    while i == j:
        # a의 구간
        while 2**i < a:
            i += 1
        # b의 구간
        while 2**j < b:
            j += 1
        
        if i == j:
            a -= 2**(i-1) 
            b -= 2**(i-1) 
            i = 0
            j = 0
    
        
    print(i,j)
    
    return max(i,j)