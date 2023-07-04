def solution(board, moves):
    cnt = 0
    check_stk = []
    
    # 반복 작동
    for i in moves:
        n = 0
        # 각 층의 i - 1열만 확인, 가장 위부터 차례로 확인.
        for j in range(len(board)):
            # 0일 때 무시, 이미 뽑은 값 0으로 초기화
            if board[j][i-1] != 0:
                # 뽑을게 있으면 추가 후 반복문 종료
                n = board[j][i-1]
                # 뽑은 인형 없애기
                board[j][i-1] = 0
                break        
        # 뽑을게 아예 없으면
        if n == 0: continue
        # 스택의 가장 상단과 뽑은 것 비교
        if check_stk and check_stk[-1] == n:
            cnt += 2
            check_stk.pop()
        else:
            check_stk.append(n)
            
    return cnt
