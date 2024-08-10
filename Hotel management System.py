
# HOTEL MANAGEMENT SYSTEM
menu = {
    'chicken' :125, 'mutton' :230, 'fish' :340, 'crab' :290
}

print("welcome to our halal resturant")
print("chicken : Rs125\nmutton :Rs230\nfish :Rs340\ncrab :Rs290")

order_total = 0
item_1 = input("enter the item you want to order= ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"ordered {item_1} has be added to your cart")
else:
    print("item not available")

another_order = input("do you want to order anything else? (yes/no)")
if another_order == "yes":
    item_2 = input("enter the item you want to order= ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"ordered {item_2} has be added to your cart")
else:
     print("item not available")

print(f"the amount to pay {order_total}")
