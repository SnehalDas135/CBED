import os
import csv

# Function to get the numeric value of a chess move from a CSV file
def get_move_value(filename, move):
    with open(filename, mode='r') as file:
        for i, line in enumerate(file):
            if line.strip().lower() == move.strip().lower():
                return i + 1  # or just i, if you want 0-based indexing
    print(f"Invalid move: {move}")
    return None
# Encryption function
def encrypt(filename):
    data = input("Enter the data to encrypt: ")
    ascii_value = [ord(char) for char in data]
    print("The person who takes white while encrypting must take white while decrypting.")
    index = 0
    while True:
        move = input("Enter your move: ")
        if move.lower() == "checkmate":
            break
        move_numeric_value = get_move_value(filename, move)
        if move_numeric_value is None:
            continue
        ascii_value[index] += move_numeric_value
        index = (index + 1) % len(ascii_value)
    encrypted_word = ''.join(chr(value) for value in ascii_value)
    print("Your encrypted value is:", encrypted_word)

# Decryption function
def decrypt(filename):
    data = input("Enter the data to decrypt: ")
    ascii_value = [ord(char) for char in data]
    print("The person who takes white while encrypting must take white while decrypting.")
    index = 0
    while True:
        move = input("Enter your move: ")
        if move.lower() == "checkmate":
            break
        move_numeric_value = get_move_value(filename, move)
        if move_numeric_value is None:
            continue
        ascii_value[index] -= move_numeric_value
        index = (index + 1) % len(ascii_value)
    decrypted_word = ''.join(chr(value) for value in ascii_value)
    print("Your decrypted value is:", decrypted_word)

# Main entry point
if __name__ == "__main__":  # <-- fixed __name__ typo
    filename = r"C:\Users\nived\Downloads\chess_variables(csv).csv"  # ensure .csv extension is correct
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found. Please check the file name and location.")
    else:
        try:
            choice = int(input("Press 1 for encryption and 2 for decryption: "))
            if choice == 1:
                encrypt(filename)
            elif choice == 2:
                decrypt(filename)
            else:
                print("Please enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")
