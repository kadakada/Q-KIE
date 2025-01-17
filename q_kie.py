
# Post Quantum Key-Independent Encryption (Q-KIE)

import random

def egcd(a, b):
    """Extended Euclidean Algorithm for finding the GCD of a and b."""
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def modinv(a, m):
    """Modular Inverse of a under modulo m."""
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m
def generate_keys(r):
    """Generate RSA public and private keys from primes p and q."""
    e = r
    while egcd(e, phi)[0] != 1:
        e += 2
    d = modinv(e, phi)
    return e , d

#---------------------------------------------------------------
# Setup Public Primitives:
p = 257
q = 65537
n = p * q
phi = (p - 1) * (q - 1)
#---------------------------------------------------------------

#Alice Secret Message:

m_1 = 41
m_2 = 5
m = [m_1, m_2]
#Alice Private Primitives:

e_1, d_1 = generate_keys(random.randrange(1, phi,2))
e_2, d_2 = generate_keys(random.randrange(1, phi,2))
r = random.randrange(1, n, 2)

#Bob Private Primitives:
e_3, d_3 = generate_keys(random.randrange(1, phi,2))
e_4, d_4 = generate_keys(random.randrange(1, phi,2))
x = random.randrange(1, 100,2)

print('Alice plaintext (m1, m2) = ', m)

#---------------------------------------------------------------

#Bob computes and sends to Alice: (c,x1,x2)

c_1 = pow(x, e_3, n)

c_2 = pow(x, e_4, n)


print('Bob sends: c1 = ', c_1, ', c2 = ', c_2)

#---------------------------------------------------------------

#Alice computes c1'' and c2''

c_3 = (pow(c_1, r, n) * pow(m_1, e_1, n))%n

c_4 = (pow(c_2, -r, n) * pow(m_2, e_2, n))%n

print('Alice sends: c3 = ', c_3, 'c4 = ', c_4)

#---------------------------------------------------------------

#Bob computes c5

c_5 = (x * pow(c_3, e_4*d_3, n) * c_4)%n
c_6 = (x * pow(c_4, e_3*d_4, n) * c_3)%n
print('Bob sends c5 = ', c_5, 'c6 = ', c_6)

#---------------------------------------------------------------

#Alice computes c6

c_7 = [None] * 2
c_8 = [None] * 2
c_7[0] = (m_1**2 * pow(c_1, -d_1, n))%n
c_8[0] = (m_2**2 * pow(c_2, -d_2, n))%n
m_2e_2 = pow(m_2, -e_2, n)
m_1e_1 = pow(m_1, -e_1, n)
c_7[1] = pow(m_2e_2 * c_5, d_1, n)
c_8[1] = pow(m_1e_1 * c_6, d_2, n)
print('Alice sends c7 = ', c_7, 'c8 = ', c_8)

#---------------------------------------------------------------

#Bob extracts m2

a = modinv((d_3 * (e_4 + 2)), phi)
c_72d_4 = pow(c_7[0], d_3, n)
mm_1 = pow(c_72d_4 * c_7[1], a, n)

b = modinv((d_4 * (e_3 + 2)), phi)
c_82d_3 = pow(c_8[0], d_4, n)
mm_2 = pow(c_82d_3 * c_8[1], b, n)
print('Bob extracts m1 = ', mm_1, 'm2 = ', mm_2)

#---------------------------------------------------------------

# A sample of the execution results
# Alice plaintext (m1, m2) =  [41, 5]
# Bob sends: c1 =  1 , c2 =  1
# Alice sends: c3 =  3246502 c4 =  3727989
# Bob sends c5 =  16591414 c6 =  11299133
# Alice sends c7 =  [1681, 14940612] c8 =  [25, 10168641]
# Bob extracts m1 =  41 m2 =  5
