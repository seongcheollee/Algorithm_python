import sys
import heapq
input = sys.stdin.readline

n = int(input())
nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))

nums.sort()

room = []
heapq.heappush(room, nums[0][1])

for i in range(1, n):
    if room[0] <= nums[i][0]:
        heapq.heappop(room)
    heapq.heappush(room , nums[i][1])

print(len(room))
