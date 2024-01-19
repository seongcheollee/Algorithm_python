def solution(s):
    res = 0
    
    # 로테이션 하는 함수
    def rotate_l(s):
        return s[1:]+s[0]
    
    # 올바른 괄호 확인하는 함수
    
    
    def check(s):
        stk = []
        
        for i in s:
            if not stk:
                stk.append(i)
            else:
                if i == ']' and stk[-1] == '[':
                    stk.pop()
                elif i == ')' and stk[-1] == '(':
                    stk.pop()
                elif i == '}' and stk[-1] == '{':
                    stk.pop()
                else:
                    stk.append(i)
    
    
        if stk:
            return 0
        else:
            return 1
        
    for i in range(len(s)):
        s = rotate_l(s)
        res += check(s)
    
        
    return  res