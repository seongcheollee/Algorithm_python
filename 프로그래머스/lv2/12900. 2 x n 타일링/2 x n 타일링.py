def solution(n):
    dp = [0,1,2,3]
    for i in range(4,n+1):
        dp.append(((dp[i-1]+dp[i-2])  % 1000000007))
    return dp[-1] 


# n = 1  -> 1
# n = 2 -> 2
# n = 3 -> 3
# n = 4 -> 5
"""

1 2 3 4 5 6 7 8 9
1 2 3 5 8 13 21 34 55   
"""
# n = 5 -> 
# 9 -> 55
print(solution(9))