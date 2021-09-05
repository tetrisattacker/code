full_name = input("What's your full name: ")
number_of_a = 0
number_of_e = 0
number_of_i = 0
number_of_o = 0
number_of_u = 0

for letter in full_name:
    if letter.lower() == 'a':
        number_of_a += 1
    elif letter.lower() == 'e':
        number_of_e += 1
    elif letter.lower() == 'i':
        number_of_i += 1
    elif letter.lower() == 'o':
        number_of_o += 1
    elif letter.lower() == 'u':
        number_of_u += 1

totals = f'''
Total number of As: {number_of_a}
Total number of Es: {number_of_e}
Total number of Is: {number_of_i}
Total number of Os: {number_of_o}
Total number of Us: {number_of_u}
Total number of letters: {number_of_a + number_of_e + number_of_i + number_of_o + number_of_u}
'''
print(totals)