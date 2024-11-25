Menu = {
    'pizza' : 100,
    'burger' : 150,
    'pasta' : 120,
    'dessert' : 50
}

print("Welcome to our restaurant!")

print("pizza: $100")

print("burger: $150")   

print("pasta: $120")

print("dessert: $50")

order_total = 0

item1 = input("Please enter the items you want to order, ")
if order in Menu:
    order_total += Menu[item1]
    print(f"You have added {item1} to your order.")

else : 
    print("Item not found in our menu.")

    another_order = input("Do you want to order anything else? (yes/no) ")

    if another_order.lower() == "yes":
        item2 = input("Please enter the items you want to order, ")
        if item2 in Menu:
            order_total += Menu[item2]
            print(f"You have added {item2} to your order.") 

    else :
        print("Item not found in our menu.")
            
        print(f"Your total order is: ${order_total}")






