#!/usr/bin/python3
"""
Module to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """Generate Pascal's triangle up to n rows."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)  # Each row starts with 1s
        if i > 1:  # Update internal values for rows greater than 2
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
