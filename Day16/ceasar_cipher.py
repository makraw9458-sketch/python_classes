# ascii table
def cipher_e(text, shift = 1):
    return "".join(chr(ord(c) + shift) for c in text)

def cipher_d(cipher, shift = 1):
    return "".join(chr(ord(c) - shift) for c in cipher)

encrypted = cipher_e("mayank123", -3)

print(encrypted)

text = cipher_d(encrypted, -3)

print(text)