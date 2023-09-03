def solution(name, yearning, photo):
    res = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning [i]

    for p in photo:
        temp = 0
        for i in p:
            if i in dic:
                temp += dic[i]
                      
                    
        res.append(temp)
    
    
    
    return res