#Make and empty the words list
words = []
#Define the prompt function with lower or not
def prompt(kind, lower=False):
    #Make the question
    ask = "Please enter "+ kind + ": "
    #Ask the quetion
    word = input(ask)
    #If lower is true then get all words with uppercase letters to all lowercase
    word = word.lower() if lower else word
    #Add the word or multiple words to the words list
    words.append(word)
#Welcome the player to my mad libs story
print("Welcome to Alex's Mab Libs Story!")
print("Get ready!")
#Execute the prompt function for stuff and add to words
prompt("your name")
print(f"Hello there, {words[0]}! Nice to meet you.")
prompt("your favorite class", lower=True)
prompt("your favorite part of that class", lower=True)
prompt("your full name")
prompt("your school name")
prompt("your first family member")
prompt("your second family member")
prompt("your third family member")
prompt("how your day was", lower=True)
#Print the story out with items from the words list
print(f"""Hi, my name is {words[0]}!
My favorite class in my school is {words[1]} because it has my favorite thing, {words[2]}!
BTW my full name is {words[3]} and my school name is {words[4]}.
And I then had dinner with my 3 special members of my family, {words[5]}, {words[6]}, and {words[7]}!
What a {words[8]} day I had!""")
#That's the end of the program that I made