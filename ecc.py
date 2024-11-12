import random
from finite_field_element import FiniteFieldElement
from point import Point
from elliptic_curve import EllipticCurve


def multiply(point, scalar):
    result = Point(None, None, point.a, point.b)
    addend = point

    while scalar:
        if scalar & 1:
            result = result + addend

        addend = addend + addend
        scalar >>= 1

    return result


class ECC:
    """Elliptic Curve Cryptography operations."""

    def __init__(self, curve, generator_point, n):
        self.curve = curve
        self.generator = generator_point
        self.n = n

    def generate_keypair(self):
        private_key = random.randint(1, self.n - 1)
        public_key = multiply(self.generator, private_key)
        return private_key, public_key

    def encrypt(self, public_key, message_point):
        k = random.randint(1, self.n - 1)
        c1 = multiply(self.generator, k)
        c2 = message_point + multiply(public_key, k)
        return c1, c2

    def decrypt(self, private_key, c1, c2):
        s = multiply(c1, private_key)
        return c2 + Point(s.x, -s.y, s.a, s.b)
