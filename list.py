cart = ["eon","nexon","polo","alto"]

print(cart[0])

print(cart[1:3])
cart.append("safari")

print(cart)

if "nexon" in cart:
    print("item present")


cart.remove("eon")   
print(cart) 


while True :
    print("\n1) ADD  \n 2) View  \n 3 )  Exit")
    choice = input("enter choice:")
    if choice =="3":
        print("exit")
        break