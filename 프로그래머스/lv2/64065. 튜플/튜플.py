def solution(s):
    res = []
    # 문자열 s를 숫자만 담긴 배열로 변환
    s = s.replace('{', '')
    s = s.split('},')
    for i in range(len(s)):
        s[i] = s[i].replace('}','')
    # print(s)
    # 문자열 길이 수에 따라 정렬 : 튜플 값의 순서를 알기 위해서
    s = sorted(s, key=len)

    # 결과 리스트에 중복된 값을 제외하고 순차적으로 값 삽입
    for i in s:
        i = i.split(',')
        for j in i:
            if not int(j) in res:
                res.append(int(j))

    return res