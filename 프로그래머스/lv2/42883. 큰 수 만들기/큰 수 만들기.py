# 문제 요약 : k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하기

# 문제풀이
# 1. 정렬 사용 불가능 -> 문자열의 순서를 지켜야함.
# 2. 앞자리부터 n-k 가 될때까지의 모든 경우의 수 구하기

# 순차적으로 넣되, 작은거만 빼주는 문제
# -> 스택 활용 문제 확인. 
def solution(number, k):

    stk = []
    # 순차적으로 확인
    for i in number:
        # 반복문을 돌면서 현재 들어갈 값보다 작은 값 pop
        while k > 0 and stk and stk[-1] < i:
            stk.pop()
            # 작은 값을 빼주었으니 k값 감소
            k -= 1
        stk.append(i)
        
    return ''.join(stk[:len(number)-k])











