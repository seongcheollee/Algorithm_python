import sys
from collections import deque
import json
input = sys.stdin.readline

T = int(input())

def check_command(command, nums):
    cnt_r = False
    for c in command:
        if c == 'R':
            cnt_r = not cnt_r
        elif c == 'D':
            if cnt_r:
                nums.pop()
            else:
                nums.popleft()


    if cnt_r:
        nums.reverse()
    return ','.join(list(nums))



for i in range(T):
    command = input()
    n = int(input())
    nums = sys.stdin.readline().rstrip()[1:-1]
    if len(nums) > 0:
        nums = deque(nums.split(','))
    else:
        nums = deque()

    if command.count('D') > len(nums):
        print('error')
        continue

    res = check_command(command, nums)
    print(f'[{res}]')


