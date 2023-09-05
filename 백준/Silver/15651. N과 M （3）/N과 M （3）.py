n, r = map(int, input().split())
number = [i for i in range(1, n + 1)]


def gen(numbers, R, current_list=[]):
    if len(current_list) == R:
        return [current_list]

    return_list = []
    for num in numbers:
        new_list = current_list + [num]
        return_list.extend(gen(numbers, R, new_list))

    return return_list


for i in gen(number, r):
    print(' '.join(map(str, i)))