new_ls = []
_, j = map(int, input().split())
ls = list(map(int, input().split()))
for i in ls:
    if i < j:
        new_ls.append(str(i))
print(' '.join(new_ls))
        