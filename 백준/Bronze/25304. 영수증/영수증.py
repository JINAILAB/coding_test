X = int(input())

# 구매한 물건의 종류의 수 입력
N = int(input())

# 계산한 총 금액 초기화
calculated_total = 0

# N개의 물건에 대해 가격과 개수 입력 후 계산
for _ in range(N):
    a, b = map(int, input().split())
    calculated_total += a * b

# 계산한 총 금액과 영수증의 총 금액 비교
if calculated_total == X:
    print("Yes")
else:
    print("No")