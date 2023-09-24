m, n = map(int, input().split())
ls = [i+1 for i in range(m)]
for i in range(n):
    a, b = map(int, input().split())
    ls[a-1:b] = ls[a-1:b][::-1]

print(' '.join(map(str, ls)))