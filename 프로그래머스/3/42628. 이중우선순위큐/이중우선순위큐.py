from collections import deque
def solution(operations):
    answer = []
    q = []
    
    for i in operations:
        oper, n = i.split(' ')
        
        if oper == 'I':
            q.append(int(n))
        else:
            if not q:
                continue

            if n == '1':
                a =  q.index(max(q))
                q.pop(a)
            else:
                a =  q.index(min(q))

                q.pop(a)
    

    if q:
        return [max(q),min(q)]
    
    return [0,0]