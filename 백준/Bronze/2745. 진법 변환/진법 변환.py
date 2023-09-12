def base_to_decimal(N, B):
    N = N[::-1]
    
    result = 0
    
    char_map = {char: idx for idx, char in enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    
    for i, char in enumerate(N):
        result += char_map[char] * (B ** i)
    
    return result

N, B = input().split()
B = int(B)
print(base_to_decimal(N, B))