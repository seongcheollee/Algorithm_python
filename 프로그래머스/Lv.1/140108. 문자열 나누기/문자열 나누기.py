def solution(s):
    answer = 0
    res = 0
    x = ''
    x_c = 0
    x_nc = 0
    temp = ''    
    for i, n in enumerate(s):
        if not x:
            x = n
            x_c += 1
            temp += n
            continue
            
        if x == n:
            x_c += 1
        else:
            x_nc += 1
        
        temp += n 

        if x_c == x_nc:
            print(temp)
            res += 1
            x = ''
            temp= ''
            
    if temp:
        res+= 1
        


    return res