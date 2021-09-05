sentence = input("Give me any sentence. ").lower()
number_of_letters = 0
number_of_vowels = 0
number_of_consonants = 0
number_of_not_vowels = 0
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']
for letter in sentence:
    if letter in letters:
        number_of_letters += 1
        if letter in vowels:
            number_of_vowels += 1
        else:
            number_of_consonants += 1
    else:
        number_of_not_vowels += 1
pronouncement = f"""There are {number_of_letters} letters in your sentence excluding symbols, numbers and spaces.
There are also {number_of_vowels} vowels and {number_of_consonants} consonants.
There are also {number_of_not_vowels} symbols, numbers and spaces."""
print(pronouncement)