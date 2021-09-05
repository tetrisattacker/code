# Program to check if a number is a prime number

num = 17

# To take input from user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

# Prime numbers are greater than 1
if num > 1:
    # Check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found set flag to True
            flag = True
            # break out of the loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")