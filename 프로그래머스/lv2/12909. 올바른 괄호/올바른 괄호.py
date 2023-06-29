def solution(s):
    # 스택 생성
    stk = []
    
    for i in s:
        # 스택에 push
        if i == "(":
            stk.append(i)
        else:
            # 스택 pop 
            if not stk or stk.pop() != "(":
                return False
            
    if stk:
        return False
    else:
        return True

