N, W, H, L = map(int, input().split())

# 헛간에서 최대로 들어갈 수 있는 소의 수 계산
max_cows_in_barn = (W // L) * (H // L)

actual_cows_in_barn = min(N, max_cows_in_barn)

print(actual_cows_in_barn)