numbers = []
for i in range(9):
    numbers.append(int(input()))

max_value = max(numbers)
max_index = numbers.index(max_value) + 1  

# 결과 출력
print(max_value)
print(max_index)