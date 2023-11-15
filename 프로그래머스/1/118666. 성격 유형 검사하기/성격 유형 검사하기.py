def solution(survey, choices):
    answer = ''

    kakao_mbti = {
        'R' : 0, 'T' : 1,
        'C' : 2, 'F' : 3,
        'J' : 4, 'M' : 5,
        'A' : 6, 'N' : 7
    }
    
    kakao_mbti_reverse = {v:k for k,v in kakao_mbti.items()} 
    res = [0 for i in range(8)]
    
    for i , val in enumerate(survey):
        n = abs(choices[i] - 4)
        # 비동의
        if choices[i] < 4:
            res[kakao_mbti[val[0]]] += n
        # 동의
        elif choices[i] > 4:
            res[kakao_mbti[val[1]]] += n
        else:
            continue
            
    for i in range(0, len(res), 2):
        if res[i] >= res[i+1]:
            answer += kakao_mbti_reverse[i]
        else:
            answer += kakao_mbti_reverse[i+1]


    return answer