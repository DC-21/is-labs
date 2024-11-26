# Initial Permutation Table
INITIAL_PERMUTATION = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
]

# Final Permutation Table
FINAL_PERMUTATION = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25,
]

# Permutation function
def permute(block, table):
    return [block[i - 1] for i in table]

# Split block into two halves
def split_block(block):
    half = len(block) // 2
    return block[:half], block[half:]

# XOR two bit arrays
def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

# Example Feistel function (simplified logic)
def feistel_function(right, subkey):
    return xor(right, subkey[:len(right)])  # XOR with subkey as a basic example

# Convert string to bit array
def string_to_bits(s):
    result = []
    for char in s:
        binval = bin(ord(char))[2:].zfill(8)  # Convert to 8-bit binary
        result.extend([int(b) for b in binval])
    return result

# Convert bit array to string
def bits_to_string(bits):
    chars = []
    for b in range(0, len(bits), 8):
        byte = bits[b:b + 8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

# DES Encryption
def des_encrypt(plain_text, key):
    # Convert plaintext and key to bits
    block = string_to_bits(plain_text)
    block = block[:64]  # Take first 64 bits (DES processes 64-bit blocks)
    key_bits = string_to_bits(key)[:64]  # Key is 64 bits

    # Initial Permutation
    block = permute(block, INITIAL_PERMUTATION)

    # Split into left and right halves
    left, right = split_block(block)

    # 16 Feistel rounds
    for _ in range(16):
        temp = right
        right = xor(left, feistel_function(right, key_bits))  # Simplified Feistel
        left = temp

    # Combine halves in reverse order
    combined = right + left

    # Final Permutation
    encrypted_block = permute(combined, FINAL_PERMUTATION)
    return bits_to_string(encrypted_block)

# Example usage
if __name__ == "__main__":
    plaintext = "HelloMrFrancis"
    key = "cholakuboko"
    encrypted = des_encrypt(plaintext, key)
    print(f"Encrypted: {encrypted}")
