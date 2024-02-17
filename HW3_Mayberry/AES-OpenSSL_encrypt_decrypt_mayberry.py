from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os


def encrypt_file(input_file_path, output_file_path, key):
    try:
        # Generate a random IV
        iv = get_random_bytes(AES.block_size)

        # Create cipher object and encrypt the data
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Read the plaintext file
        with open(input_file_path, 'rb') as f:
            plaintext = f.read()

        # Encrypt and pad the plaintext
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

        # Write the IV and ciphertext to the output file
        with open(output_file_path, 'wb') as f:
            f.write(iv + ciphertext)
        print("File encrypted successfully.")

    except FileNotFoundError:
        print("Error: The input file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def decrypt_file(input_file_path, output_file_path, key):
    try:
        # Read the IV and ciphertext from the input file
        with open(input_file_path, 'rb') as f:
            iv = f.read(AES.block_size)
            ciphertext = f.read()

        # Create cipher object and decrypt the data
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

        # Write the decrypted plaintext to the output file
        with open(output_file_path, 'wb') as f:
            f.write(plaintext)
        print("File decrypted successfully.")

    except FileNotFoundError:
        print("Error: The input file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    key = get_random_bytes(32)  # AES-256 requires a 32-byte (256 bit) key
    while True:
        action = input("Do you want to encrypt or decrypt a file? (e/d): ").strip().lower()
        if action not in ['e', 'd']:
            print("Invalid option. Please type 'e' for encrypt or 'd' for decrypt.")
            continue

        input_file_path = input("Enter the path to the input file: ").strip()
        output_file_path = input("Enter the path to the output file: ").strip()

        if action == 'e':
            encrypt_file(input_file_path, output_file_path, key)
        elif action == 'd':
            decrypt_file(input_file_path, output_file_path, key)

        # Ask user if they want to continue or exit
        cont = input("Do you want to continue? (yes/no): ").strip().lower()
        if cont != 'yes':
            break


if __name__ == "__main__":
    main()
