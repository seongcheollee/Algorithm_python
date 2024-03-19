import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    people = []
    cnt = 1
    for i in range(n):
        people.append(list(map(int, input().split())))

    people.sort()
    max_p = people[0][1]
    for i in range(1, n):
        if max_p > people[i][1]:
            max_p = people[i][1]
            cnt += 1

    print(cnt)