import math

def euclidean(c1: list[int], c2: list[int], weight: float) -> float:
    """
    Calculates the Euclidean distance between two points.

    Args:
        c1 (list[int]): The coordinates of the first point.
        c2 (list[int]): The coordinates of the second point.
        weight (float): The weight to multiply the distance by.

    Returns:
        float: The weighted Euclidean distance between the two points.
    """
    return weight * math.sqrt(((c1[0] - c2[0]) ** 2) + ((c1[1] - c2[1]) ** 2))

def manhattan(c1: list[int], c2: list[int], weight: float) -> float:
    """
    Calculates the Manhattan distance between two points.

    Parameters:
    c1 (list[int]): The coordinates of the first point.
    c2 (list[int]): The coordinates of the second point.
    weight (float): The weight to be applied to the distance.

    Returns:
    float: The weighted Manhattan distance between the two points.
    """
    return weight * (abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]))

def chebyshev(c1: list[int], c2: list[int], weight: float) -> float:
    """
    Calculates the Chebyshev distance between two points.

    Parameters:
    c1 (list[int]): The coordinates of the first point.
    c2 (list[int]): The coordinates of the second point.
    weight (float): The weight to be applied to the distance calculation.

    Returns:
    float: The weighted Chebyshev distance between the two points.
    """
    return weight * max(abs(c1[0] - c2[0]), abs(c1[1] - c2[1]))

def octile(c1: list[int], c2: list[int], weight: float) -> float:
    """
    Calculates the octile distance between two points.

    Parameters:
    c1 (list[int]): The coordinates of the first point.
    c2 (list[int]): The coordinates of the second point.
    weight (float): The weight to apply to the distance calculation.

    Returns:
    float: The octile distance between the two points.
    """
    return weight * (max(abs(c1[0] - c2[0]), abs(c1[1] - c2[1]))
            + ((math.sqrt(2) - 1) * min(abs(c1[0] - c2[0]), abs(c1[1] - c2[1]))))
