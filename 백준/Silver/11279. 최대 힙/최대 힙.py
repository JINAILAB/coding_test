import heapq
import sys
ls = []
heapq.heapify(ls)
for i in range(int(input())):
    check_input = int(sys.stdin.readline().rstrip())
    if check_input != 0:
        heapq.heappush(ls, check_input * -1)
    elif check_input == 0 and not ls:
        print(0)
    else:
        print(heapq.heappop(ls) * -1)