def solution(s):
    answer = True
    
    stk = []
    
    for i in s:
        
        if not stk:        
            if i == "(":
                stk.append(i)
            else:
                return False
        else:
            if i == ")" and stk[-1] == "(":
                stk.pop()
            else:
                stk.append(i)
        
    if stk:
        return False
                
    
    

    return True