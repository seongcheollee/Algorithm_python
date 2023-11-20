def solution(s):
    res = []

    # 압축 단위 최소 ~ 최대 범위 설정
    for i in range(1, len(s)+1):
        temp_string = ''
        cnt = 1
        check = s[:i]
        
        # i 부터 s 길이 끝만큼, i 간격
        for j in range(i,len(s),i):
            
            if check == s[j:j+i]:
                cnt += 1
            else:
                if cnt != 1:
                    temp_string += str(cnt)+check
                else:
                    temp_string += check
                check = s[j:j+i]
                cnt = 1

        if cnt != 1:
            temp_string+= str(cnt) + check
        else:
            temp_string += check
        res.append(len(temp_string))



    return min(res)

