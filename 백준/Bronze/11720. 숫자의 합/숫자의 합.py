def sum_of_digits(N, numbers):
    # Sum each digit of the number string
    return sum(int(digit) for digit in numbers)
a = int(input())
b = input()
print(sum_of_digits(a, b))