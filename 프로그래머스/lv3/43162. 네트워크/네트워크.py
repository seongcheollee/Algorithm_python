def solution(n, computers):
    answer = 0
    v = [0] * n  # Initialize visited array locally
    
    def dfs(i):
        # Check if already visited
        if v[i]:
            return 0
        # Mark as visited
        v[i] = 1

        for j in range(n):
            if computers[i][j] and not v[j]:
                dfs(j)

        return 1

    for i in range(n):
        if dfs(i):
            answer += 1

    return answer
