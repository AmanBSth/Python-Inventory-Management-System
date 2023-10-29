import read as r

model = []
company = []
price = []
quantity = []
processor = []

#stripping the text file having newline and creating a new list by splitting
with open('laptop.txt', 'r') as f:
    for line in f:
        parts = line.strip().split(',')
        model.append(parts[0])
        company.append(parts[1])
        quantity.append(parts[2])
        price.append(parts[3])
        processor.append(parts[4])

def main_logic(user_input):
    ''' contains the main logic for the program. It validates model name and quantity. 
    Returns the all the items bought by the user and total amount of it'''
    items_purchased = []
    total_amount = 0
    
    bought = False
    while not bought:
        r.readFile()
        print("\n")
        model_name = input("Please enter the name of the laptop : ").capitalize()
        print("\n")
        
        #checks if the name of the model is in the list or not
        if model_name in model:
            index = model.index(model_name)
            continue_shopping = True
            while continue_shopping:
                #validating qunatity 
                try:
                    user_quantity = input("Please enter the number of quantity : ")
                    print("\n")
                    user_quantity = int(user_quantity)
                    if user_quantity < 1:
                        print("Quantity must be at least 1")
                        print("\n")
                        continue
                    else:
                        break
                except ValueError:
                    print("Invalid quantity entered. Please enter a valid quantity.")
                    print("\n")

            if user_quantity <= int(quantity[index]):
                user_confirm = input("Are you sure you want to add?").lower()
                if user_confirm == "yes":
                    #removing the $ sign to calculate the price
                    remove_dollar = price[index].replace('$', '')
                    total_price = int(remove_dollar) * int(user_quantity)
                    if user_input == 1:
                        quantity[index] = str(int(quantity[index]) - user_quantity)
                    elif user_input == 2:
                        quantity[index] = str(int(quantity[index]) + user_quantity)
                        
                    #updating in text file
                    with open("laptop.txt", "w") as f:
                        for i in range(len(model)):
                            f.write(model[i] + "," + company[i] + "," + str(quantity[i]) + "," + price[i] + "," + processor[i] + "\n")
                    #adding the items in empty list
                    items_purchased.append([model[index], company[index], user_quantity, str(total_price), processor[index]])
                    total_amount += total_price
                # doesnt add items the empty list
                elif user_confirm == "no":
                        continue_shopping=False
            else:
                
                print("Sorry! The quantity is out of range")
        else:
            print("The laptop model you entered is not available. Please try again.")
            print("\n")
            continue
        print("\n")
        
        shop_again = input("Do you still want to add items? Yes or NO?" ).lower()
        print("\n")
        if shop_again == "no":
            break
        
    # prints the confirmed item that user purchased
    if len(items_purchased)>0:
        print("Your Confirmed Items :"+"\n")
        print("S.N.\t\t Model\t\t   Brand\t\t   Quantity\t\t  price\t\t   processors")
        print("-----------------------------------------------------------------------------------------------------------------" + "\n")
        for i in range(len(items_purchased)):
            print(str(i+1) + "\t\t " + str(items_purchased[i][0]) + "\t\t" "   "  + str(items_purchased[i][1]) + "\t\t\t " + "  " + str(items_purchased[i][2]) + "\t\t\t " + " " + "$" + str(items_purchased[i][3]) + " \t" + "  " + str(items_purchased[i][4]) + " \n")
            print("---------------------------------------------------------------------------------------------------------------" + "\n")

    return items_purchased, total_amount
        




    




    

 

