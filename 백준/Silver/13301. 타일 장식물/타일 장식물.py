n = int(input())

dp = [1,1,2]
for i in range(3,n+1):
    dp.append(dp[i-1]+dp[i-2])


print(dp[n]*2 + dp[n-1]*2)