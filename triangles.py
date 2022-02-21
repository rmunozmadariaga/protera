from typing import List, Tuple

Coords = List[Tuple[int, int]]


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    # Strategy:
    # 1 - sort the sides of both triangles and calculate their lengths

    triangle_1 = sorted([((coords_1[i][0] - coords_1[i - 1][0]) ** 2 +
                          (coords_1[i][1] - coords_1[i - 1][1]) ** 2) ** 0.5 for i in range(3)])

    triangle_2 = sorted([((coords_2[i][0] - coords_2[i - 1][0]) ** 2 +
                          (coords_2[i][1] - coords_2[i - 1][1]) ** 2) ** 0.5 for i in range(3)])

    # 2 - divide sorted lengths obtained previously
    compare_sides = [triangle_1[i] / triangle_2[i] for i in range(3)]

    print("Calculated values:")
    print('\n T1', triangle_1, '\n T2', triangle_2, '\n C', compare_sides)

    # 3 - check the values of compare_sides list are equal.
    if len(set(compare_sides)) == 1:
        # 4 - If the previous condition is True, the triangles are similar
        return True
    return False


if __name__ == '__main__':
    print("Example N1:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    print("Example N2:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]))

    print("Example N3:")
    print(similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]))

    print("Assert cases:")
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False