# Python-Inventory-Management-System
## About the program
The program is a based on a management of a laptop shop that simplifies the process
of managing and keeping track of laptop inventory, sales, and purchase orders. The
overall working of the program is divided into 4 modules i.e. Main.py, Operation.py, 
Read.py, and Write.py as per the coursework requirement. Each serves its own function 
to make the overall program work. After choosing the required process the user wants 
to perform and giving a valid input to the required details, a bill is printed in terminal and 
text file as well. The program includes error handling and validation to ensure that the
input is correct, and the program does not crash, when invalid values is given.

##  Main.py
This python file imports all the function from 3 modules to run the program. It provides 
the user options to buy, sell or exit from the system through the command line interface. 
After choosing the required option, it requires us to fill the given details with appropriate 
values and a function is called from operation.py module to perform the main logic of 
the overall program. Finally, it calls required function from write.py proceeds to print a
unique bill in the terminal and text file as well.
When an invalid number is given in the main.py options, it prints an error saying user to 
input number from the given option only and again displays the option for the user to 
select. This is done using while loop. This module also try except to handle any value 
error, preventing the program from crashing.

## Operation.py
The module contains the main logic of the overall program. It contains Read.py module 
to read each line of text file and display it for the user in formatted way. It first reads 
data from a text file containing laptop information, splits each line into separate pieces, 
and stores the pieces in separate lists for model, company, quantity, price, and 
processor.
When the user inputs valid model name and quantity from the displayed information of 
laptop, it proceeds ask user if they are sure to buy it or not. According to the required 
operation in main.py, it decreases or increases the quantity in the main text file, 
laptop.txt. At the end, it prints the confirmed item and return the item that user bought 
and total amount.

## Read.py
Read.py has a function readFile() which iterates over each line of text file and replaces 
the comma (',') with tab spaces ('\t') using the replace(). It then concatenates the 
modified line with the serial number (‘a’) using the string concatenation operator '+'. 
The serial number 'a' is then incremented by 1 and the loop continues with the next line 
until all lines in the file have been read.

## Write.py
forCustomer() function of write.py is used to print the bill of the purchased laptops by 
customer in terminal and in the text file as well. forDistributer() function is used to print 
the bill of purchased laptop by the shop from distributer in terminal and text file. It also 
imports other module such as datetime and random to generate unique bill for the user
