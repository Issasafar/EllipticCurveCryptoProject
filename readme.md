# Elliptic Curve Cryptography Project

This project implements basic elliptic curve cryptography (ECC) from scratch in Python. It includes finite field arithmetic, elliptic curve points, and ECC encryption/decryption. The implementation follows the mathematical foundations of ECC, making it suitable for educational purposes and as a foundation for further development.

## Project Structure

- **finite_field_element.py**: Implements arithmetic operations over finite fields.
- **point.py**: Defines and manages points on the elliptic curve, including operations like point addition.
- **elliptic_curve.py**: Represents the elliptic curve and provides functions for creating and managing curves.
- **ecc.py**: Provides ECC encryption and decryption functions, key generation, and core cryptographic operations.
- **main.py**: A demo script that demonstrates key generation, encryption, and decryption using the defined elliptic curve.

## Files Overview

### finite_field_element.py

Defines the `FiniteFieldElement` class, which represents elements in a finite field:

- **Attributes**: `value`, `prime`
- **Operations**: Addition, subtraction, multiplication, division, and exponentiation within the finite field.
- **Modular Arithmetic**: Handles all operations using modular arithmetic with the specified prime.

### point.py

Defines the `Point` class, representing points on an elliptic curve:

- **Attributes**: `x`, `y`, `a`, `b` (coefficients of the elliptic curve)
- **Operations**: Point addition, subtraction, and scalar multiplication based on elliptic curve group rules.
- **Special Case Handling**: Supports the "point at infinity" for representing the identity element on the elliptic curve.

### elliptic_curve.py

Defines the `EllipticCurve` class, representing an elliptic curve over a finite field:

- **Attributes**: `a`, `b` (curve coefficients), `prime` (field prime)
- **Validation**: Ensures that a point lies on the curve.
- **Point Generation**: Includes utility functions for creating points on the curve.

### ecc.py

Implements core ECC operations and cryptographic functions:

- **Key Generation**: `generate_keypair()` creates a random private key and calculates the corresponding public key point.
- **Encryption**: `encrypt(public_key, message_point)` encrypts a given point using the public key and a random multiplier.
- **Decryption**: `decrypt(private_key, c1, c2)` recovers the original message point using the private key.

### main.py

A sample script demonstrating the use of the ECC classes and functions:

- **Key Pair Generation**: Generates a random private key and corresponding public key.
- **Message Encryption and Decryption**: Demonstrates encryption and decryption of a point on the elliptic curve.
- **Output**: Displays keys, encrypted messages, and decrypted messages to verify that encryption and decryption work as expected.

## How to Run

1. Install Python 3 if not already installed.
2. Clone this repository and navigate to the project folder.
3. Run `main.py` to see ECC in action:

```bash
python main.py
