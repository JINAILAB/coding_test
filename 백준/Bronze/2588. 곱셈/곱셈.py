A = int(input())
B = input()

# B의 각 자릿수별로 A와 곱셈 수행
B_1 = int(B[2]) # 일의 자리
B_10 = int(B[1]) # 십의 자리
B_100 = int(B[0]) # 백의 자리

# 결과 출력
print(A * B_1)
print(A * B_10)
print(A * B_100)
print(A * int(B))