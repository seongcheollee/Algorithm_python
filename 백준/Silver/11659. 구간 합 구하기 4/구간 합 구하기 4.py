import sys

input = sys.stdin.readline
n, m = map(int, input().split(' '))

nums = list(map(int, input().split(' ')))
dp = [0]* (n+1)
for i in range(n):
    dp[i+1] = dp[i] + nums[i]


for i in range(m):
    a,b = map(int, input().split(' '))
    print(dp[b] - dp[a-1])
