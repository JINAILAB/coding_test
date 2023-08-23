def solution(board):
    l = len(board)
    map = [[True]*(l+2) for i in range(l +2)]
    for i in range(l):
        for j in range(l):
            if board[i][j] == 1:
                for m in (-1, 0 ,1):
                    for n in (-1, 0 ,1):
                        map[i+m+1][j+n+1] = False
    count = 0
    for i in range(1, l+1):
        for j in range(1, l+1):
            if map[i][j]:
                count += 1
    return count
                        
                
                
                  
            
            