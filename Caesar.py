def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    return ''.join(
        chr((ord(c) - (65 if c.isupper() else 97) + shift) % 26 + (65 if c.isupper() else 97)) 
        if c.isalpha() else c for c in text
    )

# Example usage
mode = input("Mode (encrypt/decrypt): ").strip().lower()
text = input("Text: ")
shift = int(input("Shift: "))
decrypt = mode == 'decrypt'

print("Result:", caesar_cipher(text, shift, decrypt))
