MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


coffees = ["latte", "espresso", "cappucino"]


is_enough = True


while True:


  coffee = input("coffee(latte/espresso/cappucino): ")


  if coffee == "report":
    

    for value,key in resources.items():
      print(value, ":", key)


  elif coffee in coffees:


    print("Please insert the coins")
    quarters = int(input("how many quarters ?"))
    dimes = int(input("how many dimes ?"))
    nickels = int(input("how many nickel?"))
    pennies = int(input("how many pennies ?"))


    coins = ((quarters * 25) + (dimes * 10) + (nickels * 5) + (pennies * 1)) / 100


    print(coins)
    if coins < MENU[coffee]["cost"]:


      print("Sorry, that's not enough money. Money refunded")


      break


    else:


      for key in resources.keys():


        if key in MENU[coffee]["ingredients"]:


          if not MENU[coffee]["ingredients"][key] < resources[key]:

          
            print("Sorry there is not enough " + key)


            is_enough = False


            break


      if is_enough == True:


        for key in resources.keys():
        
          
          if key in MENU[coffee]["ingredients"]:


            resources[key] -= MENU[coffee]["ingredients"][key]
        

        print("Here is",coins - MENU[coffee]["cost"],"in change")


        print("Here is your", coffee, "Enjoy!")

  else:


    print("please make sure you type it correctly ")

  