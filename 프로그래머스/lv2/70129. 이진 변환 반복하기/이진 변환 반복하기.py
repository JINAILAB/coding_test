def solution(s):
    cnt_bi = 0
    cnt0 = 0
    while s:
        cnt0 += s.count('0')
        s = s.replace('0', '')
        cnt_bi += 1
        s = bin(len(s))[2:]
        
        if s == '1':
            break
    return [cnt_bi, cnt0]
        
        
        
        
        