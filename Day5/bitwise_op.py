# binary operations
# the 0b prefix
# Defining binary numbers
binary_num = 0b1010  # 10 in decimal
print(binary_num)    # 10

# Different bases
print(0b1111)   # 15
print(0b1001)   # 9
print(0b110010) # 50

# Decimal to binary
num = 42
binary_str = bin(num)        # '0b101010'
binary_without_prefix = bin(num)[2:]  # '101010'

# Binary to decimal
decimal = int('101010', 2)   # 42
decimal = int(0b101010)      # 42


# Other Bases
# Octal
oct_num = 0o157
print(oct(42))     # '0o52'
print(int('52', 8)) # 42

# Hexadecimal
hex_num = 0x1abcdef
print(hex(42))     # '0x2a'
print(int('2a', 16)) # 42


# BITWISE OPERATIONS
a = 0b1010  # 10
b = 0b1100  # 12

# AND - both bits must be 1
print(bin(a & b))  # 0b1000 (8)

# OR - at least one bit is 1
print(bin(a | b))  # 0b1110 (14)

# XOR - exactly one bit is 1
print(bin(a ^ b))  # 0b0110 (6)

# NOT - flips all bits
print(bin(~a))     # -0b1011 (-11)

# Left shift (multiply by 2)
print(bin(a << 1)) # 0b10100 (20)
print(bin(a << 2)) # 0b101000 (40)

# Right shift (divide by 2)
print(bin(a >> 1)) # 0b101 (5)
print(bin(a >> 2)) # 0b10 (2)




# SOME EXAMPLES
# Check if a specific bit is set
def is_bit_set(num, position):
    return (num & (1 << position)) != 0

print(is_bit_set(0b1010, 1))  # True (bit 1 is 1)
print(is_bit_set(0b1010, 2))  # False (bit 2 is 0)

# Set a specific bit to 1
def set_bit(num, position):
    return num | (1 << position)

print(bin(set_bit(0b1000, 1)))  # 0b1010

# Clear a specific bit (set to 0)
def clear_bit(num, position):
    return num & ~(1 << position)

print(bin(clear_bit(0b1010, 1)))  # 0b1000

# Toggle a bit
def toggle_bit(num, position):
    return num ^ (1 << position)

print(bin(toggle_bit(0b1010, 1)))  # 0b1000
print(bin(toggle_bit(0b1000, 1)))  # 0b1010