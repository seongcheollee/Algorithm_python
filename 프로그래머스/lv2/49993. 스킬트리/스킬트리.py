def solution(skill, skill_trees):
    cnt = len(skill_trees)
    
    for i, sk in enumerate(skill_trees):
        skill_trees[i] = ''.join(c if c in skill else '' for c in sk)
    
    for sk in skill_trees:
        for i in range(len(sk)):
            if sk[i] != skill[i]:
                cnt -= 1
                break
        
        
        
    print(skill_trees)
    return cnt