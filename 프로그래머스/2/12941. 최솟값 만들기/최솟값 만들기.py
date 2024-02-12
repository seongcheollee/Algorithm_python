def solution(A,B):
    res = 0
    # 누적 최솟값 ->
    # list 내의 가장 작은 수와 가장 큰 수의 곱
    A.sort(reverse = False)
    B.sort(reverse = True)
    for i in range(len(A)):
        res += A[i] * B[i]
    
    return res