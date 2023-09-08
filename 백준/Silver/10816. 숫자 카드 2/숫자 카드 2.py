import sys
from collections import defaultdict

n = input()
n = map(int, sys.stdin.readline().rstrip().split())
m = sys.stdin.readline().rstrip()
m = list(map(int, sys.stdin.readline().rstrip().split()))

int_dict = defaultdict(int)

for i in n:
    int_dict[i] += 1


def convert_dict(i):
    return str(int_dict[i])


return_list = list(map(convert_dict, m))
print(' '.join(return_list))
    
