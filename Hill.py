import numpy as np

# Function to find the modular inverse of a matrix modulo 26
def mod_inverse(matrix, mod):
    det = int(np.round(np.linalg.det(matrix))) % mod
    det_inv = pow(det, -1, mod)  # Modular inverse of the determinant

    # Calculate the adjugate matrix
    adjugate = np.round(np.linalg.inv(matrix) * det).astype(int) % mod
    return (det_inv * adjugate) % mod

# Function to convert a string into numerical form (A=0, B=1, ..., Z=25)
def text_to_numbers(text):
    return [ord(c) - 97 for c in text.lower() if c.isalpha()]

# Function to convert numerical form back to a string
def numbers_to_text(numbers):
    return ''.join(chr(num + 97) for num in numbers)

# Encrypt a plaintext using the Hill Cipher
def hill_cipher_encrypt(plaintext, key_matrix):
    text_numbers = text_to_numbers(plaintext)
    while len(text_numbers) % key_matrix.shape[0] != 0:
        text_numbers.append(0)  # Padding with 'A' (0)

    # Encrypt each block
    ciphertext = []
    for i in range(0, len(text_numbers), key_matrix.shape[0]):
        block = np.array(text_numbers[i:i + key_matrix.shape[0]]).reshape(-1, 1)
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext.extend(encrypted_block.flatten())

    return numbers_to_text(ciphertext)

# Decrypt a ciphertext using the Hill Cipher
def hill_cipher_decrypt(ciphertext, key_matrix):
    text_numbers = text_to_numbers(ciphertext)
    inverse_key_matrix = mod_inverse(key_matrix, 26)

    # Decrypt each block
    plaintext = []
    for i in range(0, len(text_numbers), key_matrix.shape[0]):
        block = np.array(text_numbers[i:i + key_matrix.shape[0]]).reshape(-1, 1)
        decrypted_block = np.dot(inverse_key_matrix, block) % 26
        plaintext.extend(decrypted_block.flatten())

    return numbers_to_text(plaintext)

# Example usage
if __name__ == "__main__":
    # Example 2x2 key matrix
    key_matrix = np.array([[6, 24], [1, 16]])

    mode = input("Mode (encrypt/decrypt): ").strip().lower()
    text = input("Text: ").strip()

    if mode == 'encrypt':
        encrypted_text = hill_cipher_encrypt(text, key_matrix)
        print("Encrypted Text:", encrypted_text)
    elif mode == 'decrypt':
        decrypted_text = hill_cipher_decrypt(text, key_matrix)
        print("Decrypted Text:", decrypted_text)
    else:
        print("Invalid mode. Choose 'encrypt' or 'decrypt'.")
