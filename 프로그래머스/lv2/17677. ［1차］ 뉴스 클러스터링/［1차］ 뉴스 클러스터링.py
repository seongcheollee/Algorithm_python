# 문제 요약 : 나올 수 있는 두자리 수의 알파벳 조합을 통해서 자카드 유사도 값 계산 교집합 / 합집합. 공집합 = 1
"""
문제 풀이
1. 문자열 소문자로 통일
2. 공백 제거
3. 각 문자열 별로 나올 수 있는 알파벳 조합 찾기
4. set() 을 통해서 중복 제거
5. 교집합, 합집합 개수 구하기
6. 자카드 유사도 사용
"""
def solution(str1, str2):
    #소문자로 통일
    str1 = str1.lower()
    str2 = str2.lower()
    # 길이 2로 분할
    str1_j = [str1[i]+str1[i+1] for i in range(len(str1)-1)]
    str2_j = [str2[i]+str2[i+1] for i in range(len(str2)-1)]
    
    res1 = []
    res2 = []
    # 알파벳으로 이루어진 것만 결과 리스트에 담기
    for i in str1_j:
        if not " " in i and i.isalpha():
            res1.append(i)
    for i in str2_j:
        if not " " in i and i.isalpha():
            res2.append(i)

    # & | 는 집합 연산자에서 and , or 로 작동
    intersec = set(res1) & set(res2)
    union = set(res1) | set(res2)

    # 합집합이 0 인 경우 처리
    if not len(union):
        return 65536
    
    # 문제에서 제시된 유사도 공식 적용 (개별 값에 대한 min 값의 합)
    inter_l = sum([min(res1.count(i), res2.count(i)) for i in intersec])
    # 문제에서 제시된 유사도 공식 적용 (개별 값에 대한 max 값의 합)
    union_l = sum([max(res1.count(u), res2.count(u)) for u in union])

    
    return int(inter_l/union_l * 65536)
