shape = input("Enter a shape. Triangle(a) or Quadrilateral(b)? ")
a = int(input("Select a value for a: "))
b = int(input("Select a value for b: "))
c = int(input("Select a value for c: "))
if shape == "b":
    d = int(input("Select a value for d: "))
    s = (a + b + c + d) / 2
    area = (s * (s - a) * (s - b) * (s - c) * (s - d)) ** 0.5
    if any(all(a == b, c == d), all(a == c, b == d), all(a == d, b == c)):
        print("The name of this quadrilateral is either a rectangle or a parerrellogram. And...")
    elif any(a == b and c > d, a == b and c < d, a == c and b > d, a == c and b < d, a == d and b > c, a == d and b < c):
        print("The name of this quadrilateral is a trapezoid. And...")
    elif a == b == c == d:
        print("The name of this quadrilateral is either a square or a rhombus. And...")
    else:
        print("This is just an ordinary quadrilateral. But...")
    print("The area of this quadrilateral is {0}!".format(area))
else:
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    if any(a == b, a == c, b == c):
        print("The name of this triangle is an Isoceles Triangle. And...")
    elif all(a == b, a == c, b == c):
        print("The name of this triangle is an Equilateral Triangle. And...")
    else:
        print("This is just an ordinary triangle. But...")
    print("the area of this triangle is %0.2f!" %area)