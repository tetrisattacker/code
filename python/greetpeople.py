def greet(name, is_new):
    if is_new:
        print(f"Hello, {name}! Nice to meet you!")
    else:
        print(f"What's up, {name}? Nice to see you again!")

name = input("What is your name? ")
is_new = input("True or False? ")
greet(name, is_new)