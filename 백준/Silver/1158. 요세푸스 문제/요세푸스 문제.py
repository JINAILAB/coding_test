from collections import deque

n, k = map(int, input().split())


def josephus(n, k):
    circle = deque(range(1, n + 1))
    result = []

    while circle:
        circle.rotate(-(k - 1))
        result.append(circle.popleft())

    return result


josephus = josephus(n, k)

print('<'+str(josephus)[1:-1]+'>')