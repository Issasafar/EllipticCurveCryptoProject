from finite_field_element import FiniteFieldElement


class EllipticCurve:
    """Defines an elliptic curve for cryptographic operations."""

    def __init__(self, a, b, prime):
        self.a = a
        self.b = b
        self.prime = prime

    def is_on_curve(self, x, y):
        """Check if a point (x, y) is on the elliptic curve."""
        return (y ** 2) % self.prime == (x ** 3 + self.a * x + self.b) % self.prime

    def __repr__(self):
        return f"EllipticCurve(a={self.a}, b={self.b}, prime={self.prime})"
