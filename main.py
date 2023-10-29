import write as w
import operation as o

loop = True
while loop:
    # Printing the option to perform user need
    print("------------------------------------------------------------------" +"\n")
    print("Given below are some of the options for you to carryout the needed")
    print("\n")
    print("Enter 1 to sell laptop to your customer")
    print("Enter 2 to purchase from Manufacturer")
    print("Enter 3 to Exit from the system")
    print("\n")
    print("------------------------------------------------------------------")
    print("\n")
    
    try:
        user_input = int(input("Enter the option to continue: "))
        
    except ValueError:
        print("\n")
        print("Invalid option. Please enter a number from the given option. Thank You" +"\n")
        continue
    
    if user_input == 1:
        print("\n")
        print("Please enter the customer's details: ")
        print("\n")
        #validating correct names
        while True:
            first_name = input("Enter the customer's first name: ")
            if first_name.isalpha():
                break
            else:
                print("\n")
                print("Invalid first name. Please enter a valid name with only alphabets.")
                print("\n")
        while True:
            last_name = input("Enter the customer's last name: ")
            if last_name.isalpha():
                break
            else:
                print("\n")
                print("Invalid last name. Please enter a valid name with only alphabets.")
                print("\n")
                
        address = input("Enter the customer's address: ")
        print("\n")
        shipping_cost=1000
        items_purchased,total_amount=o.main_logic(user_input)
        #generates only the bill if the length of the item is greater than 0
        if len(items_purchased)>0:
            ship_choice = input("Would the customer like to ship the laptops?").lower()
            if ship_choice == "yes":
                total_amount += shipping_cost
            elif ship_choice == "no":
                shipping_cost = 0
            # generating bill in text file
            w.for_customer(first_name, last_name, address, items_purchased,shipping_cost)

        else:
            continue

    elif user_input==2:
        print("\n")
        print("Please enter the following details details: ")
        print("\n")
        shop_name=input("Enter your shop name : ")
        distributer_name = input("Enter the name of the distributer: ")
        address = input("Enter your address: ")
        print("\n")
        items_purchased,total_amount=o.main_logic(user_input)
        # generating bill in text file
        w.for_distributer(items_purchased,distributer_name,shop_name,address)

    #terminating the program
    elif user_input==3:
        print("Thank You for your time !")
        break

    else:
        print("\n")
        print("Invalid option. Please enter a number from the given option. Thank You")

    
        

    
