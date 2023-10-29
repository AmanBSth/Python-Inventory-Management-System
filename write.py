
import datetime
import random
import operation as o


def currentDate():
    ''' generates current date'''
    current_time = datetime.datetime.now()
    return str(current_time.date())


def currentTime():
    ''' generates current time '''
    current_time = datetime.datetime.now()
    time_str = str(current_time.time())
    return time_str.replace(':', '_')


def randomNumber():
    '''generating random number'''
    randomNum = random.randrange(100000000, 1000000000)
    return str(randomNum)

#generating bill for customer in terminal and text
def for_customer(firstName, lastName, address, items_bought,shipping_cost):
    ''' The function is used to generate unique bill both in shell and text file. It takes the parameter from main.py'''
    customer = firstName + "'s Bill " + "_" + currentTime() + ".txt"
    total_price = 0
    for item in items_bought:
        total_price += int(item[3])

    print("======================================================================================================" + "\n" + "\n")
    print("\t \t \t \t \t \t Shrestha Electronic Store")
    print("\t \t \t \t Kamalpokhari, Kathmandu | Phone Number: 9847378792" + "\n" + "\n")
    print("Sold To      : " + " " + firstName + " " + lastName)
    print("Address      : " + " " + address)
    print("Bill Number  : " + " " + randomNumber())
    print("Purchased On : " + " " + currentDate() + "   " + currentTime() + "\n" +"\n" )
    print("S.N.\t\t Model\t\t   Brand\t\t   Quantity\t\t  price\t\t ")
    print("----------------------------------------------------------------------------------------------------" + "\n")

    #prints the items that user purchased
    for i in range(len(items_bought)):
        print(str(i+1) + "\t\t " + str(items_bought[i][0]) + "\t\t" + "   "  + str(items_bought[i][1]) + "\t\t\t " + "  " + str(items_bought[i][2]) + "\t\t\t " + " " + "$" + str(items_bought[i][3])+ " \n")
        print("---------------------------------------------------------------------------------------------------" + "\n")

    print("Total Amount without shipping cost : " + "$" + str(total_price))
    print("Total shipping cost                : " + "$" + str(shipping_cost))
    print("-------------------------------------------" +"\n")
    print("Total Amount                       : " + "$" + str(shipping_cost+total_price) + "\n" + "\n")
    print("\t \t \t \t \t \t Thank you for shopping with us!" +"\n")
    print("====================================================================================================="+ "\n")

    #printing th bill in text file
    with open(customer, "w") as f:
        f.write("==========================================================================================="+ "\n")
        f.write("\n"+"\n")
        f.write("\t\t\t\t\tShrestha Electronic Store\n")
        f.write("\t\t\t\tKamalpokhari, Kathmandu | Phone Number: 9847378792\n\n")
        f.write("Sold To      : " + firstName + " " + lastName + "\n")
        f.write("Address      : " + address + "\n")
        f.write("Purchased On : " + currentDate() + " " + currentTime() + "\n")
        f.write("Bill Number  : " + randomNumber())
        f.write("\n\n")
        f.write("S.N.\t\t Model\t\t   Brand\t\t   Quantity\t\t  price\t\t " +"\n")
        f.write("----------------------------------------------------------------------------------" + "\n")

        # Print items purchased
        for i in range(len(items_bought)):
            f.write(str(i+1) + "\t\t " + str(items_bought[i][0]) + "\t\t" + "   "  + str(items_bought[i][1]) + "\t\t " + "  " + str(items_bought[i][2]) + "\t\t\t" + "  " + "$" + str(items_bought[i][3]) +" \n")
            f.write("--------------------------------------------------------------------------------" + "\n")
            
        # Print total amount
        f.write("\n\n\n")
        f.write("Total Amount without shipping cost : $" + str(total_price)+"\n")
        f.write("Total Shipping Cost                : $" + str(shipping_cost)+"\n")
        f.write("-------------------------------------------" +"\n")
        f.write("Total Amount After Shipping        : $" + str(total_price) + "\n")
        f.write("\n\n")
        f.write("\t \t \t \t \t \t Thank you for shopping with us!" )
        f.write("\n\n")
        f.write("======================================================================================"+ "\n")
        f.close()

    

def for_distributer(items_bought,distributer_Name,shopName,address):
    ''' The function is used to generate unique bill both in shell and text file.
    It takes the parameter from main.py'''
    
    total_price = 0
    shop=distributer_Name +"'s Bill"+ "_"+ currentTime()+".txt"
    for item in items_bought:
        total_price += int(item[3])
    print("======================================================================================================" + "\n" + "\n")
    print("\t \t \t \t \t \t "+  distributer_Name + "\n\n\n")
    print("Sold to      : " + " " + shopName)
    print("Address      : " + " " + address)
    print("Purchased On : " + " " + currentDate() + "   " + currentTime())
    print("Bill Number  : " + " " + randomNumber() +"\n\n\n" )
    print("S.N.\t\t Model\t\t   Brand\t\t   Quantity\t\t  price\t\t ")
    print("-------------------------------------------------------------------------------------------------------" + "\n")

    #prints the items that user purchased
    for i in range(len(items_bought)):
        print(str(i+1) + "\t\t " + items_bought[i][0] + "\t\t" "   "  + items_bought[i][1] + "\t\t\t " + "  " + str(items_bought[i][2]) + "\t\t\t " + " " + "$" + str(items_bought[i][3]) + " \n")
        print("--------------------------------------------------------------------------------------------------------" + "\n")
        
    print("\n")
    print("Net Amount                   : " + "$"+str(total_price))
    print("VAT Amount                   : " + "$"+str((13*total_price)/100))
    print("--------------------------------------")
    print("Gross Amount                 : " + "$"+str(total_price+  (13*total_price)/100)+"\n"+"\n")
    print("***13% VAT Added" +"\n\n")
    print("\t \t \t \t \t \t Thank you for shopping with us!" )
    print("\n")
    print("========================================================================================================"+ "\n") 

    #printing th bill in text file
    with open(shop, "w") as s:
        s.write("============================================================================================"+ "\n\n\n") 
        s.write("\t\t\t\t\t\t" +distributer_Name + "\n\n\n")
        s.write("Sold to      : " + shopName + "\n")
        s.write("Address      : " + address +"\n")
        s.write("Purchased On : " + currentDate() + " " + currentTime() + "\n")
        s.write("Bill Number  : " + randomNumber()+"\n\n")
        s.write("\n\n")
        s.write("S.N.\t\t Model\t\t   Brand\t\t   Quantity\t\t  price\t\t "+"\n")
        s.write("---------------------------------------------------------------------------------------" + "\n")

        # Print items purchased
        for i in range(len(items_bought)):
            s.write(str(i+1) + "\t\t " + str(items_bought[i][0]) + "\t\t" + "   "  + str(items_bought[i][1]) + "\t\t " + "  " + str(items_bought[i][2]) + "\t\t\t" + "  " + "$" + str(items_bought[i][3])+ " \n")
            s.write("-------------------------------------------------------------------------------------------" + "\n")

        # Print total
        s.write("\n\n\n")
        s.write("Total Amount             : $" + str(total_price)+"\n")
        s.write("VAT Amount               : $"+ str((13*total_price)/100)+"\n")
        s.write("---------------------------------\n")
        s.write("Gross Amount             : $" + str((13*total_price)/100 +total_price))
        s.write("\n\n")
        s.write("***13% VAT Added" +"\n\n")
        s.write("\t \t \t \t \t \t Thank you for shopping with us!" )
        s.write("\n\n")
        s.write("============================================================================================="+ "\n")
        s.close()





       






     
     
