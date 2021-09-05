sentence = input("Give me any sentence. ").lower()
number_of_letters = 0
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for letter in sentence:
    if letter in letters:
        number_of_letters += 1
pronouncement = f"There are {number_of_letters} letters in your sentence excluding symbols, numbers and spaces."
print(pronouncement)