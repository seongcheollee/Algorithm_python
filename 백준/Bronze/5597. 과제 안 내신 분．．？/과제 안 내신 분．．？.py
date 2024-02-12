check = [0] * 30

for i in range(28):
    check[int(input())-1] = 1

for i in range(30):
    if not check[i]:
        print(i+1)