def solution(line):
    points = []
    int_y_points = []
    int_x_points = []
    for i in line:
        for j in line:
            if i[0] * j[1] == i[1] * j[0]:
                continue
            else:
                points.append([(i[1]*j[2]-i[2]*j[1])/(i[0]*j[1]-i[1]*j[0]), (i[2]*j[0] - i[0]*j[2])/(i[0]*j[1]-i[1]*j[0])])
    for point in points:
        if (int(point[0]) == point[0]) and (int(point[1]) == point[1]):
            int_x_points.append(int(point[0]))
            int_y_points.append(int(point[1]))

    int_x_points = list(map(lambda x: x - min(int_x_points), int_x_points))
    int_y_points = list(map(lambda x: x - min(int_y_points), int_y_points))

    point_map = [['.'] * (max(int_x_points)+1) for i in range(max(int_y_points)+1)]

    for i, j in zip(int_x_points, int_y_points):
        point_map[j][i] = '*'

    for i in range(len(point_map)):
        point_map[i] = ''.join(point_map[i])

    return point_map[::-1]