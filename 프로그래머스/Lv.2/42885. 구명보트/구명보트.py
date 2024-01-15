def solution(people, limit):
    res = 0
    people.sort(reverse=True)
    stk = []
    
    for i in people:
        if not stk:
            stk.append(i)
            continue

        if stk[-1] + i <= limit:
            stk.pop()
            res += 1
        else:        
            stk.append(i)

    
    
    return res + len(stk)