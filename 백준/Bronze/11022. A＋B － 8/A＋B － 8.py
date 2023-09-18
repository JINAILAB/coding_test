import sys

def sum_and_print(test_cases):
    results = []
    for idx, (a, b) in enumerate(test_cases, start=1):
        results.append(f"Case #{idx}: {a} + {b} = {a+b}\n")
    return results

test_cases = [tuple(map(int, sys.stdin.readline().rstrip().split())) for i in range(int(input()))]

print(''.join(sum_and_print(test_cases)))