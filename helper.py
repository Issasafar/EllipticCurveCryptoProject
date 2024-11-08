from math import isqrt

from finite_field_element import FiniteFieldElement
from point import Point


def get_points_on_curve(curve, prime):
    """
    Generate all points (x, y) that lie on the given elliptic curve over a finite field.

    Parameters:
        curve (EllipticCurve): The elliptic curve (contains a and b).
        prime (int): The prime number that defines the finite field.

    Returns:
        List of Points: All valid (x, y) points on the curve.
    """
    points = []

    for x in range(prime):
        x_field_element = FiniteFieldElement(x, prime)

        # Calculate the right side of the elliptic curve equation: y^2 = x^3 + ax + b
        rhs = x_field_element ** 3 + curve.a * x_field_element + curve.b

        # Check if there's a y such that y^2 = rhs
        for y in range(prime):
            y_field_element = FiniteFieldElement(y, prime)
            if y_field_element ** 2 == rhs:
                points.append(Point(x_field_element, y_field_element, curve.a, curve.b))

    # Include the point at infinity
    points.append(Point(None, None, curve.a, curve.b))

    return points
