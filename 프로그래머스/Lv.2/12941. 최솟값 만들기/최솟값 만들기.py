def solution(A,B):
    res = 0
    A.sort()
    B.sort(reverse=True)
    print(B)
    for i in range(len(A)):
        res += A[i] * B[i]
    
    return res