print("* Welcme to our restro here's the menu * - special offer -- There is 10% of discount in ordering 3 or more than 3 items:")
menu = {"Pasta":50,
        "Pizza":120,
        "Salad":70,
        "Coffee":80,
        "Tea":40,
        "Burger":60,
        "Chicken":200,
        "Rice":150,
        "Water":20,
        "Chowmein":60,
        "Momos":60,
        "Roti":7}
print("Pizza:Rs120\nPasta:Rs50\nBurger:Rs60\nchowmein:Rs60\nMomos:Rs60\nCoffee:Rs80\nTea:Rs40\nChicken:Rs200\nRice:Rs150\nRoti:Rs7\nSalad:Rs70\nwater:Rs20")
order = {} 
print("***If you did not want to order press no otherwise enter your meal***")
while True:
    choice = input("What will you have:")
    capitalize = choice.lower().capitalize()
    if choice == "no":
       break
    elif capitalize in menu:
        order[capitalize] = menu[capitalize]
    else:
        print("Sorry",choice,"not present in our menu please do another order!")
print("Your Items are added")
print("Your order is ",order)
if len(order) >= 3:
   total = sum(order.values()) -  (sum(order.values())//10)
   print("## Your total price is -",sum(order.values()),"RS")
   print("You buyed",len(order),"items so you got the 10% of discount on your total price now you have to pay:",total,"RS Only")
else:  
  print("## Your Total price is -",sum(order.values()),"RS Only")
print("~~~~ Thanks for having your meal in our restro ~~~~")