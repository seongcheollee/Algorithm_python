from collections import defaultdict

dic = defaultdict(list)

T = int(input())
sign = []
for i in range(T):
    age, name = input().split(' ')
    sign.append((int(age),name))

sign.sort(key=lambda x:x[0])

for i in sign:
    print(i[0], i[1])