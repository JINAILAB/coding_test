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
n, r = map(int, input().split())
number = [i for i in range(1, n + 1)]
for i in permutations(number, r):
    print(' '.join(map(str, i)))