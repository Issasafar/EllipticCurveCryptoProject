class FiniteFieldElement:
    """Represents an element in a finite field."""
    def __init__(self, value, prime):
        self.value = value % prime
        self.prime = prime

    def __add__(self, other):
        assert self.prime == other.prime, "Cannot add elements of different fields"
        return FiniteFieldElement(self.value + other.value, self.prime)

    def __sub__(self, other):
        assert self.prime == other.prime, "Cannot subtract elements of different fields"
        return FiniteFieldElement(self.value - other.value, self.prime)

    def __mul__(self, other):
        assert self.prime == other.prime, "Cannot multiply elements of different fields"
        return FiniteFieldElement(self.value * other.value, self.prime)

    def __pow__(self, exponent):
        n = exponent % (self.prime - 1)
        return FiniteFieldElement(pow(self.value, n, self.prime), self.prime)

    def __truediv__(self, other):
        assert self.prime == other.prime, "Cannot divide elements of different fields"
        inv = pow(other.value, self.prime - 2, self.prime)
        return FiniteFieldElement(self.value * inv, self.prime)

    def __eq__(self, other):
        if other is None:
            return False
        return self.value == other.value and self.prime == other.prime

    def __repr__(self):
        return f"FiniteFieldElement({self.value}, {self.prime})"

    def __neg__(self):
        """Returns the additive inverse of the element in the finite field."""
        return FiniteFieldElement(-self.value, self.prime)
