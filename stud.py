shopping_cart= [ ]

print("menu")


shopping_cart.append("realme")
shopping_cart.append("chainlube")
shopping_cart.append("keychain")
shopping_cart.append("bikecover")

print(shopping_cart)

shopping_cart.remove("realme")
print(shopping_cart)


shopping_cart[1] = "pillow"
print(shopping_cart)

for index ,item in enumerate (shopping_cart):
    print(f"item {index}:{item}")

item_search = "pillow"
if item_search in shopping_cart:
    print(f"Found {item_search} at index {shopping_cart.index( item_search)}")

else :

    print(f" {item_search} not found at position")     














