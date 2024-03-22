


l, c = map(int , input().split())

aeiou = ['a','e','i','o','u']

alpha = list(map(str, input().split()))
alpha.sort()

res = []
stk = []
def dfs(s):

    if len(stk) == l:
        cnt = 0
        for k in aeiou:
            if k in stk:
                cnt += 1
        if l - cnt > 1 and cnt > 0:
            res.append(''.join(stk))
        return

    for i in range(s, c):
        stk.append(alpha[i])
        dfs(i+1)
        stk.pop()


dfs(0)
print('\n'.join(res))