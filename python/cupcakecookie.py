def dessert_sorter(desserts):
    for i in range(desserts):
        if i % 5 == 0 and i % 3 == 0:
            print("cupcakecookie")
        elif i % 5 != 0 and i % 3 == 0:
            print("cupcake")
        elif i % 5 == 0 and 1 % 3 != 0:
            print("cookie")
dessert_sorter(200)