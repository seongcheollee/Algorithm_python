n = int(input())
sCard = list(map(int, input().split(' ')))
m = int(input())
checkCard = list(map(int, input().split(' ')))

sCard.sort()

def binary(num):
    low = 0
    high = n -1
    while low <= high:
        mid = (low + high) // 2
        if sCard[mid] == num:
            return 1
        elif sCard[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return 0

for num in checkCard:
    print(binary(num), end =' ')