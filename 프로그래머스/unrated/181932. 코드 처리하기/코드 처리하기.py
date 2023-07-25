def solution(code):
    mode = 0
    ret = ''
    
    for i in range(len(code)):
        if code[i] == '1':
            if mode == 1:
                mode = 0
            else:
                mode = 1
            continue
            
        if i % 2 == 0 and mode == 0:
            print(i)
            ret += code[i]
        
        if i % 2 == 1 and mode == 1:
            print(i)
            ret += code[i]
            
    return ret if ret else "EMPTY"


