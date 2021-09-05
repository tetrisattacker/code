number = input("Say any number that is less than 100 but more than 1. ")
prime = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '73', '79', '83', '91', '97']
if number in prime:
    print("Your number is prime.")
else:
    print("Your number is composite.")