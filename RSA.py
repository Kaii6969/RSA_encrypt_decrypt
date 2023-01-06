import math
import random

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(e, tot):
    g, x, y = egcd(e, tot)
    return x % tot

def estPremier(n):
    if n == 2 or n == 3:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def genererCles(p, q):
    n = p * q
    n_prime = (p - 1) * (q - 1)
    e = random.randint(3, n_prime - 1)
    while math.gcd(e, n_prime) != 1:
        e = random.randint(3, n_prime - 1)
    d = modinv(e, n_prime)
    return ((n, e), (n, d))

def encoderMessage(message, public_key):
    encoded = []
    for char in message:
        encoded.append(pow(ord(char), public_key[1], public_key[0]))
    return encoded

def decoderMessage(encoded_message, private_key):
    decoded = ''
    for number in encoded_message:
        decoded += chr(pow(number, private_key[1], private_key[0]))
    return decoded


# Génération des clés
p = 0
q = 0
while not estPremier(p):
    p = random.randint(100000000000, 1000000000000000)
while not estPremier(q) or q == p:
    q = random.randint(100000000000, 1000000000000000)
clePrivee, clePublique = genererCles(p, q)
# Demande du message à coder
message = input("Entrez le message à coder : ")
print("Message original :", message)

# Encodage du message 
messageEncode = encoderMessage(message, clePublique)
print("Message encodé :", messageEncode)

# Decodage du message
messageDecode = decoderMessage(messageEncode, clePrivee)
print("Message décodé :", messageDecode)