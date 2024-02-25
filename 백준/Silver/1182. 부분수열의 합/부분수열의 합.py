import sys
input = sys.stdin.readline

n, s = map(int , input().split(' '))
nums = list(map(int , input().split(' ')))
stk = []
cnt = 0

def dfs(c):
    global cnt

    if sum(stk) == s and len(stk) > 0:
        cnt += 1

    for i in range(c,n):
        stk.append(nums[i])
        dfs(i+1)
        stk.pop()

dfs(0)
print(cnt)