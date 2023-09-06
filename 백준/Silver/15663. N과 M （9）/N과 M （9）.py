from itertools import combinations, permutations


def find_sequences(M, numbers):
    numbers.sort()

    combs = combinations(numbers, M)

    result = []
    for comb in combs:
        result.extend(permutations(comb, M))

    result = sorted(set(result))
    return result


n, m = map(int, input().split())
numbers = list(map(int, input().split()))


for i in find_sequences(m, numbers):
    print(' '.join(map(str, i)))