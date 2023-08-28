n, m = map(int, input().split())
def combinations_memo(n, m, memo={}):
    if m == 0 or m == n:
        return 1
    if (n, m) in memo:
        return memo[(n, m)]
    else:
        memo[(n, m)] = combinations_memo(n-1, m-1, memo) + combinations_memo(n-1, m, memo)
        return memo[(n, m)]
    
print(combinations_memo(n, m))
