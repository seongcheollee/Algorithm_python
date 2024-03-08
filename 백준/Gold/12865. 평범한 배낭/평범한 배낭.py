n , k = map(int, input().split(' '))

# w , v
obj = [[0,0]]
knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(n):
    obj.append(list(map(int, input().split(' '))))


for i in range(1,n+1):
    w = obj[i][0]
    v = obj[i][1]
    for j in range(1,k+1):
        if  w <= j:
            knapsack[i][j] = max(v + knapsack[i-1][j-w],knapsack[i-1][j] )
        else:
            knapsack[i][j] = knapsack[i - 1][j]

print(knapsack[n][k])