import random
import time
add = lambda a, b : a + b
sub = lambda a, b : a - b
mul = lambda a, b : a * b
exp = lambda a, b : a / b
question_number = 1

while question_number < 10:
    print(f"Question number {question_number}:")
    num1 = random.randint(-10, 10)
    num2 = random.randint(-10, 10)
    operation_number = random.randint(1, 4)
    if operation_number == 1:
        operation = "+"
        correct_answer = add(num1, num2)
        question = f"What is {num1} {operation} {num2}? "
    elif operation_number == 2:
        operation = "-"
        correct_answer = sub(num1, num2)
        question = f"What is {num1} {operation} {num2}? "
    elif operation_number == 3:
        operation = "*"
        correct_answer = mul(num1, num2)
        question = f"What is {num1} {operation} {num2}? "
    else:
        operation = "**"
        num2 = 2
        correct_answer = exp(num1, num2)
        question = f"What is {num1} {operation} {num2}? "
    question_guess = input(question)
    if question_guess == correct_answer:
        print("Correct!")
    else:
        print("Wrong!")
    seconds = input("How many seconds of break? ")
    print(f"There will now be a {seconds} second break.")
    time.sleep(seconds)
    question_number += 1
print("Hope you had fun at the 10Q math quiz! Have a nice day!")