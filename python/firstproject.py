password = 'cupcakes'
guess = ''
secret_message = 'Tommorow, I will bring cookies for me and you to share!'
while guess != password:
    print('What is the password?')
    guess = input()
print(f"Correct password! The secret message is {secret_message}")