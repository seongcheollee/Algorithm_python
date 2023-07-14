def solution(s):
    stk = []

    for i in range(len(s)):
        if not stk or stk[-1] != s[i]:
            stk.append(s[i])
        else:
            stk.pop()
        
    if stk:
        return 0
    else:
        return 1
    
    
