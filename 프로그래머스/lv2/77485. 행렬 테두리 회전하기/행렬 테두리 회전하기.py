def rotate(matrix, query):
    y0, x0, y1, x1 = map(lambda x: x - 1, query)
    mem = matrix[y0][x0]
    find_min = [mem]
    for i in range(y0, y1):
        matrix[i][x0] = matrix[i + 1][x0]
        find_min.append(matrix[i][x0])
    for i in range(x0, x1):
        matrix[y1][i] = matrix[y1][i + 1]
        find_min.append(matrix[y1][i])
    for i in range(y1, y0, -1):
        matrix[i][x1] = matrix[i - 1][x1]
        find_min.append(matrix[i - 1][x1])
    for i in range(x1, x0+1, -1):
        matrix[y0][i] = matrix[y0][i - 1]
        find_min.append(matrix[y0][i - 1])
    matrix[y0][x0 + 1] = mem
    return matrix, min(find_min)


def solution(rows, columns, queries):
    matrix = []
    for j in range(1, rows + 1):
        matrix.append([i + (j - 1) * columns for i in range(1, columns + 1)])

    result = []
    for query in queries:
        matrix, min_mat = rotate(matrix, query)
        result.append(min_mat)

    return result
        
    
        
