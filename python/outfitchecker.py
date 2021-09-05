cher_dress_color = 'pink'
cher_shoe_color = 'white'
cher_has_earrings = True
dionne_dress_color = 'purple'
dionne_shoe_color = 'pink'
dionne_has_earrings = True
print(f"Both girls have different dress colors? {cher_dress_color != dionne_dress_color}")
print(f"Both girls are wearing earrings? {cher_has_earrings and dionne_has_earrings}")
print(f"At least one person is wearing pink? {cher_dress_color == 'pink' or dionne_dress_color == 'pink'}")
print(f"No one is wearing green? {cher_dress_color != 'green' and dionne_dress_color != 'green'}")
print(f"Both girls have the same shoe color? {cher_shoe_color == dionne_shoe_color}")