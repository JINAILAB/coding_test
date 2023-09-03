n, r = map(int, input().split())
nums = [i+1 for i in range(n)]

def gen_combinations(nums, R, current_perm=[]):
    if len(current_perm) == R:
        return [current_perm]

    combinations = []
    for i, num in enumerate(nums):
        next_perm = current_perm + [num]
        remaining_nums = nums[i + 1:]
        combinations.extend(gen_combinations(remaining_nums, R, next_perm))

    return combinations


for i in gen_combinations(nums, r, []):
    i = map(str, i)
    print(' '.join(i))