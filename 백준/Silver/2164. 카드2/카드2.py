from collections import deque

que = deque(range(1, int(input()) + 1))

for i in range(len(que)-1):
    que.popleft()
    que.rotate(-1)

print(que.popleft())