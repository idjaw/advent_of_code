def is_valid_triangle(triangle):
    triangle.sort()
    return triangle[0] + triangle[1] > triangle[2]


def valid_triangle_count(triangles):
    count = 0
    for triangle in triangles:
        if is_valid_triangle(triangle):
            count += 1
    return count
