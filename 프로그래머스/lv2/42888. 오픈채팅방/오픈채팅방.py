# Enter와 Leave에 대해서만 출력
# Change 작업시 변경
# Change 작업의 유형 -> 1. 그냥 변경 2. 나갔다 들어오기


def solution(record):
    res = []
    nickName = {}
    for r in record:
        temp = r.split(' ')
        if temp[0] != 'Leave':
            nickName[temp[1]] = temp[2]
    
    for r in record:
        temp = r.split(' ')
        res_str = ''
        if temp[0] ==  'Enter':
            res_str = nickName[temp[1]]+"님이 들어왔습니다."
        elif temp[0] == 'Leave':
            res_str = nickName[temp[1]]+"님이 나갔습니다."
        else:
            continue
        res.append(res_str)        
        
    
    return res