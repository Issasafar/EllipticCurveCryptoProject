from finite_field_element import FiniteFieldElement
from point import Point
from elliptic_curve import EllipticCurve
from ecc import ECC

# Define the curve parameters
prime = 223
a = FiniteFieldElement(0, prime)
b = FiniteFieldElement(7, prime)

# Set up curve and generator point
curve = EllipticCurve(a, b, prime)
generator_point = Point(FiniteFieldElement(15, prime), FiniteFieldElement(86, prime), a, b)
n = 223  # Order of the generator point

# Instantiate ECC
ecc = ECC(curve, generator_point, n)

# Key generation
private_key, public_key = ecc.generate_keypair()
print(f"Private key: {private_key}")
print(f"Public key: {public_key}")

# Message encryption
message_point = Point(FiniteFieldElement(192, prime), FiniteFieldElement(105, prime), a, b)
c1, c2 = ecc.encrypt(public_key, message_point)
print(f"Encrypted message: (c1={c1}, c2={c2})")

# Message decryption
decrypted_point = ecc.decrypt(private_key, c1, c2)
print(f"Original message: {message_point}")
print(f"Decrypted message: {decrypted_point}")


