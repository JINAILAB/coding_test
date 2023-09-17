def int_type_name(N):
    long_count = N // 4
    return ' '.join(['long'] * long_count + ['int'])

print(int_type_name(int(input())))