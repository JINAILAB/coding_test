def solution(s):
    s = s.lstrip('{{').rstrip('}}').replace(',', ' ').split('} {')
    s = sorted(s, key=lambda x: len(x))
    answer = []
    for i in range(len(s)):
        s[i] = set(map(int, s[i].split()))
    ss = [set()]
    ss.extend(s)
    for i in range(len(ss) - 1):
        answer.append(list((ss[i + 1] - ss[i]))[0])

    return answer
        
    
    
    