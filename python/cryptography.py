plaintext_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ciphertext_letters = []
for i in range(len(plaintext_letters) - 1):
    ciphertext_letters.append(plaintext_letters[i + 1])
ciphertext_letters.append('a')
ciphertext = input("Enter your code you would like others to decipher: ")
plaintext = ""
for letter in range(len(ciphertext_letters)):
    plaintext += ciphertext_letters[letter]
guess = input("What is the plaintext? ")
if guess == plaintext:
    print("That's the correct plaintext!")
else:
    print(f"Aww, the plaintext was {plaintext}.")