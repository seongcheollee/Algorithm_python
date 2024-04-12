def solution(msg):    
    msg = msg.upper()
    dic = {}
    res = [0]
    val = 26
    base = ''
    for i in range(1,val+1):
        dic[chr(64+i)] = i
        
    for s in msg:
        base += s
        
        if base in dic:
            res[-1] = dic[base]
        else:
            val += 1
            dic[base] = val
            base = s
            res.append(dic[base])
            
    return res
            
    
    


print(ord('A'),ord('Z'))