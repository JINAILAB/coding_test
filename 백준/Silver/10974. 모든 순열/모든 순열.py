
from itertools import permutations

n = int(input())

def print_permutations(N):
    perms = permutations(range(1, N + 1))

    result = []
    for perm in sorted(perms):
        result.append(' '.join(map(str, perm)))
    return result



for i in print_permutations(n):
    print(i)