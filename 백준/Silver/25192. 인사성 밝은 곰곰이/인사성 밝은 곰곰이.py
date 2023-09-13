import sys

input = sys.stdin.readline
"""
ENTER이후 중복이 없는 자료구조에 저장 (set)
ENTER를 입력받을 때 마다 ENTER를 초기화
  +) set에 있는 개수를 ans에 추가.
"""

N = int(input())
s = set()
ans = 0
input()

for i in range(N - 1):
  user = input().strip()
  if user == "ENTER":
    ans += len(s)
    s.clear()
  else:
    s.add(user)
ans += len(s)

print(ans)