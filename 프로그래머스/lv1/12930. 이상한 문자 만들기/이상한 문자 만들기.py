def solution(s):
    words = s.split(' ')
    res = []
    
    for word in words:
        temp = ''
        for i,t in enumerate(word):
            if i % 2 == 0:
                temp += t.upper()
            else:
                temp += t.lower()

        res.append(temp)
    print(res)
    return ' '.join(res)