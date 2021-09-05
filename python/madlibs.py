words = []
def prompt(kind):
    ask = "Please enter "+ kind + ": "
    word = input(ask)
    words.append(word)
print("Welcome to Alex's Mab Libs Story!")
print("Get ready!")
prompt("your name")
prompt("your favorite class")
prompt("your favorite part of that class")
prompt("your full name")
prompt("your school name")
prompt("your first family member")
prompt("your second family member")
prompt("your third family member")
prompt("how your day was")
print(f"""Hi, my name is {words[0]}!
My favorite class in my school is {words[1]} because it has my favorite thing, {words[2]}!
BTW my full name is {words[3]} and my school name is {words[4]}.
And I then had dinner with my 3 special members of my family, {words[5]}, {words[6]}, and {words[7]}!
What a {words[8]} day I had!""")