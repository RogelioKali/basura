def gcd(a, b):
    # Compute the greatest common divisor (GCD) of a and b using the Euclidean algorithm
    while b:
        a, b = b, a % b
    return a

def is_primitive_root(g, n, phi, prime_factors):
    # Check if g is a primitive root modulo n
    for factor in prime_factors:
        # If g^(phi/factor) ≡ 1 (mod n) for any factor, then g is not a primitive root
        if pow(g, phi // factor, n) == 1:
            return False
    return True

def find_all_primitive_roots(n):
    if n == 1:
        # For n = 1, there are no primitive roots, return an empty list
        return []
    if n == 2:
        # For n = 2, the only primitive root is 1
        return [1]
    
    # Calculate Euler's totient function φ(n) = n - 1 for prime n
    phi = n - 1
    prime_factors = set()
    
    # Find all prime factors of φ(n)
    m = phi
    for i in range(2, int(m**0.5) + 1):
        if m % i == 0:
            prime_factors.add(i)
            while m % i == 0:
                m //= i
    if m > 1:
        prime_factors.add(m)

    primitive_roots = []
    for g in range(2, n):
        # Check if g is a primitive root modulo n
        if is_primitive_root(g, n, phi, prime_factors):
            primitive_roots.append(g)
    
    return primitive_roots

# Example usage:
n = 7
primitive_roots = find_all_primitive_roots(n)
print(f"All primitive roots modulo {n} are: {primitive_roots}")
