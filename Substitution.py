def substitution_cipher(text, key, decrypt=False):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_map = str.maketrans(key if not decrypt else key[::-1], alphabet if not decrypt else alphabet[::-1])
    return text.lower().translate(key_map)

# Example usage
mode = input("Mode (encrypt/decrypt): ").strip().lower()
text = input("Text: ").strip()
key = input("Substitution Key (26 unique letters): ").strip().lower()

if len(key) != 26 or len(set(key)) != 26:
    print("Invalid key. It must have 26 unique letters.")
else:
    print("Result:", substitution_cipher(text, key, decrypt=(mode == 'decrypt')))
