def solution(s):
    ss = list(s.split(' '))
    
    for i in range(len(ss)):
        ss[i] = ss[i].capitalize()
     
    return " ".join(ss)