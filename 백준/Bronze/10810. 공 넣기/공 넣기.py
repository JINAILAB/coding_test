from collections import defaultdict

n, m = map(int, input().split())
int_dict = defaultdict(int)
for i in range(m):
    start, end, bucket_num = map(int, input().split())
    for j in range(start, end+1):
        int_dict[str(j)] = bucket_num

for i in range(1, n+1):
    print(int_dict[str(i)])