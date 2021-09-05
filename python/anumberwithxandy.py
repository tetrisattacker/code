x = 0
x_in_range = int(input("What would you like the first number to be: "))
y_in_range = int(input("What would you like the second number to be: "))

loops = abs(max(x_in_range, y_in_range))


if x_in_range < 0 and y_in_range < 0:
    number = max(abs(x_in_range), abs(y_in_range))
else:
    number = max(x_in_range, y_in_range)

for i in range(number):
    x += number
print(f"The answer of multiplying {x_in_range} and {y_in_range}, we get {x}!")