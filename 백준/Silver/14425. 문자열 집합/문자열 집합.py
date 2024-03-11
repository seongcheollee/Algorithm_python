n ,m = map(int, input().split())

st_set = []
for i in range(n):
    st_set.append(input())

cnt = 0

for i in range(m):
    t = input()
    if t in st_set:
        cnt += 1

print(cnt)