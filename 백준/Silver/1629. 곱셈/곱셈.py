def pow(a, b, c):

    if b == 1:
        return a % c

    v = pow(a, b // 2, c)
    if b % 2 == 0:
        return v * v % c

    return v * v * a % c

a,b,c = map(int, input().split(' '))

print(pow(a,b,c))

