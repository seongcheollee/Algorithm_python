n, m = map(int, input().split(' '))
tree = list(map(int, input().split(' ')))
low = 1
high = max(tree)

while low <= high:
    mid = (low + high) // 2
    res = 0
    for i in tree:
        if i >= mid:
            res += i - mid
    if res >= m:
        low = mid + 1
    else:
        high = mid - 1
print(high)
