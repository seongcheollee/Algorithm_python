

def combination(n, m):
    # 2차원 배열 생성 및 초기화
    dp = [[0] * (m+1) for _ in range(n+1)]

    # 기저 사례 초기화
    for i in range(n+1):
        dp[i][0] = 1

    # 점화식 계산
    for i in range(1, n+1):
        for j in range(1, min(i, m)+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    return dp[n][m]

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    print(combination(m, n))

