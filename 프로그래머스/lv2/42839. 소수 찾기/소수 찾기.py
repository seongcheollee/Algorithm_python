# 문제 요약 : 문자열에 적힌 정수를 가지고 만들 수 있는 조합 중 소수 찾기
# 특이점 : 중복 존재, 길이 7로 제한.

# 풀이 방향성
# 1. numbers로 각 숫자들의 조합으로 만들 수 있는 경우의 수
# 2. 소수를 확인하는 isPrime() 과 dfs or bfs를 통해서 소수인 경우 count -> 구현 실패
# 3. permutations 함수 사용

from itertools import permutations

def solution(numbers):
    cnt = 0
    res = []
    # 모든 순열 조합 생성
    n_list = [list(permutations(numbers, i)) for i in range(1,len(numbers)+1) ]

    # 각 순열의 값들을 합쳐서 숫자로 변환
    for i in n_list:
        for j in i:
            res.append(int(''.join(map(str, j))))
    # 중복 제거        
    res = list(set(res))
    # 카운트
    for i in res:
        cnt += isPrime(i)
    return cnt
    
def isPrime(n):
    if n < 2:
        return 0 
    for i in range(2, n):
        if n % i == 0:
            return 0    
    return 1







