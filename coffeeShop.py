import barista


def checkout(order):
    print("Order was picked up")


def menu():
    menuList = (f"1) Cafe Au Lait\n2) Cappuccino\n3) Espresso\n4) Exit")
    print(f"Welcome to coffee shop!")
    print(menuList)
    while True:
        try:
            order = input("Please select an order: ")
            if(order == "1" or order.lower() == "cafe au lait"):
                print(f"You ordered Cafe Au Lait!")
                barista.work(order)
            elif(order == "2" or order.lower() == "cappuccino"):
                print(f"You ordered Cappuccino!")
                barista.work(order)
            elif(order == "3" or order.lower() == "espresso"):
                print(f"You ordered Espresso!")
                barista.work(order)
            elif(order == "4" or order.lower() == "exit"):
                break
            else:
                print(f"We are sorry. That is not on our menu. Please try again")
                print(menuList)
        except ValueError:
             print(f"We are sorry. That is not on our menu. Please try again")
            
    print(f"Please come again!")
    exit(0)

if __name__ == "__main__":
    menu()