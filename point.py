from finite_field_element import FiniteFieldElement


class Point:
    """Represents a point on an elliptic curve."""

    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y

        # Point at infinity
        if self.x is None and self.y is None:
            return

        if self.y ** 2 != self.x ** 3 + a * self.x + b:
            raise ValueError(f"Point ({x}, {y}) is not on the curve")

    def __eq__(self, other):
        return (self.x, self.y, self.a, self.b) == (other.x, other.y, other.a, other.b)

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError("Points are not on the same curve")

        if self.x is None:
            return other
        if other.x is None:
            return self

        if self.x == other.x and self.y != other.y:
            return self.__class__(None, None, self.a, self.b)

        if self.x != other.x:
            s = (other.y - self.y) / (other.x - self.x)
            x = s ** 2 - self.x - other.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)

        if self == other:
            s = (FiniteFieldElement(3, self.a.prime) * self.x ** 2 + self.a) / (
                        FiniteFieldElement(2, self.a.prime) * self.y)
            x = s ** 2 - FiniteFieldElement(2, self.a.prime) * self.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)

    def __repr__(self):
        if self.x is None:
            return "Point at Infinity"
        return f"Point(x={self.x}, y={self.y}) on Curve y^2 = x^3 + {self.a}x + {self.b}"
