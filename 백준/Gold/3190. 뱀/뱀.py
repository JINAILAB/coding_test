import sys
from collections import deque

N = int(input())
board = [[0] * N for _ in range(N)]
dir_changes = deque()
# 사과를 2로 기록
for _ in range(int(sys.stdin.readline())):
    y, x = map(int, sys.stdin.readline().rstrip().split())
    board[y-1][x-1] = 2
for _ in range(int(sys.stdin.readline())):

    y, x = sys.stdin.readline().rstrip().split()
    dir_changes.append((int(y), x))

# 1. 맵 밖으로 나가거나 자기 자신을 만나면 종료
# 2. 뱀의 위치는 board 상에서 1로 기록
# 3. time이 +1될 때마다 한 칸 이동
# - 이동했을 때 맵 위치에서 벗어나거나 자기 자신 즉, 1을 만나면 종료
# - 만약 아니라면, 사과가 있는 지 탐색 없으면 뒤에를 하나 줄임. 있으면 추가
# - 마지막으로 방향을 바꾸어야 하는지 아닌지 확인


def game_over(board, dir_changes):
    time = 0
    dirs = 0
    # 우, 하, 좌, 상
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # snake는 (0,0)에서 시작
    snake = deque([(0, 0)])
    board[0][0] = 1
    while True:
        time += 1
        head = snake[0]
        ny, nx = head[0] + dy[dirs], head[1] + dx[dirs]

        # 1. 맵 밖으로 나가거나 자기 자신을 만나면 종료
        if nx < 0 or nx >= N or ny < 0 or ny >= N or board[ny][nx] == 1:
            return time
        # 사과를 먹는 경우
        if board[ny][nx] == 2:
            board[ny][nx] = 1
            snake.appendleft((ny, nx))
        # 먹지 않는 경우
        else:
            board[ny][nx] = 1
            snake.appendleft((ny, nx))
            ty, tx = snake.pop()
            board[ty][tx] = 0

        # 방향 바꾸어야하는지 아닌지 확인
        if dir_changes:
            if dir_changes[0][0] == time:
                if dir_changes[0][1] == 'D':
                    dirs = (dirs + 1) % 4
                    dir_changes.popleft()
                else:
                    dirs = (dirs - 1) % 4
                    dir_changes.popleft()


print(game_over(board, dir_changes))