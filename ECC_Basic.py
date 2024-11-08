import random


# a point on the elliptic curve
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + ', ' + str(self.y)


class EllipticCurveCryptography:
    def __init__(self, a, b):
        # y^2 = x^3 + ax + b
        # Bitcoin - a=0 and b=7 (y^2 = x^3 +7)
        self.a = a
        self.b = b

    def point_addition(self, p, q):
        x1, y1 = p.x, p.y
        x2, y2 = q.x, q.y

        # sometimes we have to make a point addition
        # and sometimes a point doubling (p=q)
        if x1 == x2 and y1 == y2:
            # point doubling operation
            m = (3 * x1 * x1 + self.a) / (2 * y1)
        else:
            m = (y2 - y1) / (x2 - x1)

        # we have update x3 and y3
        x3 = m * m - x1 - x2
        y3 = m * (x1 - x3) - y1

        return Point(x3, y3)

    # this function has O(m) linear running time complexity
    def double_and_add(self, n, p):
        temp_point = Point(p.x, p.y)
        # skip the first digit and the 0b
        binary = bin(n)[3:]
        for binary_char in binary:
            # point double operation
            temp_point = self.point_addition(temp_point, temp_point)
            if binary_char == '1':
                # point addition operation
                temp_point = self.point_addition(temp_point, p)

            return temp_point


if __name__ == '__main__':
    ecc = EllipticCurveCryptography(a=0, b=7)
    # the E elliptic curve + the G generator is public
    generator_point = Point(-2, -1)

    # Alice random number (a)
    alice_random = random.randint(1, pow(10, 4))

    # Bob random number (b)
    bob_random = random.randint(1, pow(10, 4))

    # public key with double and add algorithm
    # these are points on the elliptic curve
    alice_public = ecc.double_and_add(alice_random, generator_point)
    bob_public = ecc.double_and_add(bob_random, generator_point)

    # they can generate the private key (which will be the same)
    alice_secret_key = ecc.double_and_add(alice_random, bob_public)
    bob_secret_key = ecc.double_and_add(bob_random, alice_public)
    print(alice_secret_key)
    print(bob_secret_key)
