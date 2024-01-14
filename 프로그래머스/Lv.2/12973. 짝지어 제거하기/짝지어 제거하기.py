def solution(s):
    stk = []
    
    for i in s:
        # 스택 빔
        if not stk:
            stk.append(i)
        elif stk[-1] == i:
            stk.pop()
        else:
            stk.append(i)

            
    if stk:
        return 0
    else:
        return 1
        
    
    return answer