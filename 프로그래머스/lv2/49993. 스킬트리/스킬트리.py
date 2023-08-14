# 문제접근
# 각 스킬 트리에서 스킬순서에 필요한 알파벳만 필터링 한후
# 해당 스킬트리의 길이를 기준으로(중복이 없기 때문에 필터링된 스킬트리는 선행스킬 문자열보다 길이가 짧거나 같아야하고, 인덱스에 따른 값또한 일치해야함.) 선행스킬과 맞는지 판별. 

def solution(skill, skill_trees):
    
    # 값을 빼주기 위해서 스킬트리의 길이만큼 카운트 변수 할당
    cnt = len(skill_trees)
    
    # 선행스킬과 관련없는 문자 필터링
    for i, sk in enumerate(skill_trees):
        skill_trees[i] = ''.join(c if c in skill else '' for c in sk)
    
    # 필터링된 스킬트리를 기준으로 일치여부 판독
    for sk in skill_trees:
        for i in range(len(sk)):
            if sk[i] != skill[i]:
                cnt -= 1
                break
              
 #   print(skill_trees)
    return cnt