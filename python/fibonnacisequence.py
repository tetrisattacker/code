def fibonacci_sequence(count, nterms):
    fibonacci_sequence_numbers = []
    # Program to display the Fibonacci sequence up to n-th term
    number_of_terms = nterms
    # first two terms
    n1, n2 = 0, 1
    count_in_function = count
    # check if the number of turn is valid
    if number_of_terms <= 0:
        print("Please enter a positive integer")
    # if there is only one turn, return n1
    elif number_of_terms == 1:
        print("Fibonacci sequence upto",number_of_terms,":")
        print(n1)
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence:")
        while count_in_function < number_of_terms:
            print(n1)
            fibonacci_sequence_numbers.append(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
fibonacci_sequence(0, int(input("How many terms would you like? ")))