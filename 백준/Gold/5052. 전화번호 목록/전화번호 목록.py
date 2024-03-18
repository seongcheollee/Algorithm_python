import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    phone = []
    ans = ''

    for i in range(n):
        phone.append(input().rstrip())
    phone.sort()

    for i in range(n-1):
        if phone[i] == phone[i+1][:len(phone[i])]:
            ans = 'NO'


    if ans == 'NO':
        print('NO')
    else:
        print('YES')
