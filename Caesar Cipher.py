def encrypt(text, shift):
    """
    Encrypts the given text using Caesar Cipher with the specified shift.
    
    Parameters:
    text (str): The plaintext to be encrypted.
    shift (int): The number of positions to shift each character.
    
    Returns:
    str: The encrypted ciphertext.
    """
    encrypted_text = []
    
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)

def decrypt(text, shift):
    """
    Decrypts the given text using Caesar Cipher with the specified shift.
    
    Parameters:
    text (str): The ciphertext to be decrypted.
    shift (int): The number of positions to shift each character back.
    
    Returns:
    str: The decrypted plaintext.
    """
    decrypted_text = []
    
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)

def main():
    print("Caesar Cipher Encryption and Decryption")
    
    while True:
        print("\nMenu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            plaintext = input("Enter the plaintext: ")
            shift = int(input("Enter the shift value: "))
            ciphertext = encrypt(plaintext, shift)
            print(f"Encrypted Text: {ciphertext}")
        elif choice == '2':
            ciphertext = input("Enter the ciphertext: ")
            shift = int(input("Enter the shift value: "))
            plaintext = decrypt(ciphertext, shift)
            print(f"Decrypted Text: {plaintext}")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

