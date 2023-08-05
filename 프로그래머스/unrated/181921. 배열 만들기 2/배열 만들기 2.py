# 5의 배수
# 5와 0외의 다른 숫자가 들어간 5의 배수 제거

def solution(l, r):
    answer = []
    check = 0
    # 5의 배수만큼 반복문
    for i in range(l,r+1):
        # 문자열로 변경하여 자리수 마다 0 또는 5외의 숫자가 있는지 확인 
        for j in str(i):
            if j != '0' and j != '5':
                # 해당 문자열 탐색 후 끝내야하기 때문에 check 변수로 확인
                check = 1
                break
                
        if not check:
            answer.append(i)
        check = 0
        
        
    return  answer if answer else [-1]