#!/usr/bin/python3
def pascal_triangle(n):
    """returns a pascal's triangle of a list of lists of integers

    Args:
        n (int): Number of rows for Pascal's Triangle.

    Returns:
        list: List of lists representing Pascal's Triangle
    """
    if n <= 0:
        return []

    triangles = [[1]]

    while len(triangles) != n:
        p_tri = triangles[-1]
        temp = [1]
        for i in range(len(p_tri) - 1):
            temp.append(p_tri[i] + p_tri[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
