# Enter와 Leave에 대해서만 출력
# Change 작업시 변경
# Change 작업의 유형 -> 1. 그냥 변경 2. 나갔다 들어오기


def solution(record):

    res = []
    # 해시 사용
    nickName = {}
    
    # 각 record에서 닉네임 변경에 관여하는 것은 "Enter", "Change"
    # 해당 동작이 수행될 때 마다, uid 키의 값을 갱신
    for r in record:
        temp = r.split(' ')
        if temp[0] != 'Leave':
            nickName[temp[1]] = temp[2]
    
    # 출력문 리스트 삽입
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