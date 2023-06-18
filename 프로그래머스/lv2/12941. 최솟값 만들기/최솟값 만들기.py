def solution(A,B):
    res = 0
    A.sort(reverse = False)
    B.sort(reverse = True)
    for i in range(len(A)):
        res += A[i] * B[i]
    
    return res