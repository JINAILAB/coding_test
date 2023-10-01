def solution(n):
    def spiral_matrix(n):
        matrix = [[0] * n for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_idx = 0
        num = 1
        i, j = 0, 0
        while num <= n * n:
            matrix[i][j] = num
            num += 1
            next_i, next_j = i + directions[direction_idx][0], j + directions[direction_idx][1]
            if 0 <= next_i < n and 0 <= next_j < n and matrix[next_i][next_j] == 0:
                i, j = next_i, next_j
            else:
                direction_idx = (direction_idx + 1) % 4
                i, j = i + directions[direction_idx][0], j + directions[direction_idx][1]
        return matrix
    
    return spiral_matrix(n)