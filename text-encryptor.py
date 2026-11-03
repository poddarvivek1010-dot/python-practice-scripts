# Text encryptor - (Caesar Cipher)


def caesar_cipher(text, shift, encrypt=True):
    if not isinstance(shift, int) or isinstance(shift, bool):
        return "Error: Shift parameter must be a pure integer."

    if shift < 1 or shift > 25:
        return "Error: Shift range must stay between 1 and 25."

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Reversing the index direction if decrypting
    if not encrypt:
        shift = -shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    translation_table = str.maketrans(
        alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper()
    )
    return text.translate(translation_table)


# Script Verification
original_message = "Vivek Kumar practicing advanced Python logic blocks."
print(f"Original Text: {original_message}")

# Encrypting text using a fixed mathematical key pattern
encrypted_payload = caesar_cipher(original_message, 13, encrypt=True)
print(f"Encrypted System Data: {encrypted_payload}")

# Decrypting data payload back to clean string format
decrypted_payload = caesar_cipher(encrypted_payload, 13, encrypt=False)
print(f"Decrypted System Data: {decrypted_payload}")
