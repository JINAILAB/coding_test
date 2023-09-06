import sys


def permutations(numbers, R, current_list=[]):
    if len(current_list) == R:
        return [current_list]

    if not numbers:
        return []

    results = []
    for idx, num in enumerate(numbers):
        chosen = current_list + [num]
        remaining_numbers = numbers[:idx] + numbers[idx + 1:]
        results.extend(permutations(remaining_numbers, R, chosen))

    return results


# Test for n=4, r=4
number_dict = {}
n, r = map(int, input().split())
number = [i for i in range(1, n + 1)]
print_numbers = list(map(int, sys.stdin.readline().rstrip().split()))
print_numbers.sort()

for i, j in zip(number, print_numbers):
    number_dict[i] = j


for i in permutations(number, r):
    print(' '.join(list(map(str, [number_dict[j] for j in i]))))