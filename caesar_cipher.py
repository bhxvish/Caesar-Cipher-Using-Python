def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - offset + shift * (1 if encrypt else -1)) % 26 + offset)
        else:
            result += char
    return result

def encrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as file:
        text = file.read()
        encrypted_text = caesar_cipher(text, shift)

    with open(output_file, 'w') as file:
        file.write(encrypted_text)

def decrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as file:
        text = file.read()
        decrypted_text = caesar_cipher(text, shift, encrypt=False)

    with open(output_file, 'w') as file:
        file.write(decrypted_text)
