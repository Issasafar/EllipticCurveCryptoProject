import random

from finite_field_element import FiniteFieldElement
from helper import get_points_on_curve
from point import Point
from elliptic_curve import EllipticCurve
from ecc import ECC

# Define the curve parameters
prime = 223
a = FiniteFieldElement(0, prime)
b = FiniteFieldElement(7, prime)

# Set up curve and generator point
curve = EllipticCurve(a, b, prime)
# Generate points on the curve
points = get_points_on_curve(curve, prime)
print("Points on the curve:")
i = 0
for point in points:
    print(f"Index {i}:  {point}")
    i += 1

generator_point = Point(FiniteFieldElement(15, prime), FiniteFieldElement(86, prime), a, b)
n = 223  # Order of the generator point

# Instantiate ECC
ecc = ECC(curve, generator_point, n)

# Key generation
# Generate key pair
private_key, public_key = ecc.generate_keypair()
print(f"Private key: {private_key}")
print(f"Public key: {public_key}")

# Encrypt a sample message (represented as a point)
temp_point = Point(FiniteFieldElement(192, prime), FiniteFieldElement(105, prime), a, b)
message_point = points[9]
c1, c2 = ecc.encrypt(public_key, message_point)
print(f"\nOriginal message: {message_point}")
print("\nEncrypted message:")
print(f"  Cipher Point 1 (c1): {c1}")
print(f"  Cipher Point 2 (c2): {c2}")

# Decrypt the message
decrypted_point = ecc.decrypt(private_key, c1, c2)
print(f"\nDecrypted message: {decrypted_point}")

