s = input('')
t = input('')

res = 0
        
def dfs(t):
    global res

    if t == s:
        res = 1
        
    if len(t) == 0:
        return 0

    if t[-1] == 'A':
        dfs(t[:-1])
        
    if t[0] == 'B':
        dfs(t[1:][::-1])
    

dfs(t)

if res:
    print(1)
else:
    print(0)

