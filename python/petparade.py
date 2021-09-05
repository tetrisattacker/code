pet_parade_order = ['Pete the Pug', 'Sally the Siamese Cat', 'Beau the Boxer', 'Lulu the Labrador', 'Lily the Lynx', 
'Pauline the Parrot', 'Gina the Gerbil', 'Tubby the Tabby Cat']
print(f"So far the pet parade order is like this: {pet_parade_order}")
print("But wait! A good thing has happened! Gina just got adopted so she doesn't have to be in he pet parade!")
pet_parade_order.remove("Gina the Gerbil")
print(f"Now the pet parade is this: {pet_parade_order}")
print("Pauline should be in front because he can say hello to the viewers because he's a parrot.")
del(pet_parade_order[5])
pet_parade_order.insert(0, "Pauline the Parrot")
print(f"It's now like this: {pet_parade_order}")
print("Bad news. More pets.")
pet_parade_order[6:6] = ["Mimi the Maltese Cat", "Cory the Corgi"]
print("Lulu and Lily are adopted too!")
del(pet_parade_order[4:6])
print (f"This is the end pet parade: {pet_parade_order}")