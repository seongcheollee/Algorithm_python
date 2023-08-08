def solution(n):
    res = ''
    # 0 1 2 인덱스
    nList = [1,2,4]
    
    # 3진법 활용
    while n > 0:
        # 0 이 카운트 되지 않기 때문에, n - 1
        # 즉 124 나라에서 1은 , 3진법의 계산법으로 0과 같음
        n -= 1
        t = str(nList[n % 3])
        n = n // 3
        res += t
    
    #앞자리 0 제거
    if n != 0:
        res += str(n)

    # reverse
    res = res[::-1]
    
    return res

