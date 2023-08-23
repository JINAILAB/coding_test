def solution(lines):
    lens = 0
    ll= []
    lines = [[j for j in range(i[0], i[1])] for i in lines]
    for i in lines:
        ll.append(set(i))
    return len((ll[0] & ll[1]) | (ll[1] & ll[2]) | (ll[2] & ll[0]))
            
                    
            