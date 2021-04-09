# 1. set p,q
# 2. n = p * q
# 3. phi(n) = (p - 1) * (q - 1)
# 4. find e : gcd(phi(n), e) = 1, 1 < e < phi(n)
# 5. find d : e * d mod phi(n) = 1, 1 < d < phi(n)
# 6. encrypt
# 7. decrypt

from math import gcd

def setting(p: int , q: int):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = find_e(phi_n)
    d = find_d(phi_n, e)
    
    return n, e, d

def find_e(phi_n: int):
    e = 0
    for i in range(2, phi_n):
        if gcd(phi_n, i) == 1:
            e = i
            break
    
    return e

def find_d(phi_n: int, e : int):
    d = 0
    for i in range(2, phi_n):
        if (e * i) % phi_n == 1:
            d = i
            break
        
    return d

def encrypt(plain_text: str, pub_key: list):
    plain_o = 
    plain_bytes = [int(x, 16) for x in plain_text]
    cipher_byte = []
    
    for i in plain_bytes:
        cipher_byte.append((i ** pub_key[1] % pub_key[0]))
        
    return cipher_byte

#복원단계
def decrypt(cipher_list: list, pri_key: list):
    
    plain_bytes = []
    for i in cipher_list:
        plain_bytes.append((i ** pri_key[1] % pri_key[0]))
        
    plain_text = "".join([chr(x) for x in plain_bytes])
    
    return plain_text
    
if __name__=="__main__":
    p = 11
    q = 13
    n, e, d = setting(p, q)
    
    pub_key = [n, e]
    pri_key = [n, d]
    
    plain = "0x4d765050762d2162592d1512043e813e6e6e"
    
    cipher = encrypt(plain, pub_key)
    print(cipher)
    
    
    dec_plain = decrypt(cipher, pri_key)
    print(dec_plain)