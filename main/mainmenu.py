from add import *               #1
from search import *            #2
from update import *            #3
from delete import *            #4
from profitloss import *        #5
from show import *              #6
from bill import *              #7

print("\n\t\t\t\t\t\t\t\t\t\t\t\t   ++=> WELCOME <=++\n")

while True:   # To avoid program crash due to typos

    try:
        main = str(input("Are you a customer or an employee? [c] / [e]: "))
        
        if main in "cC" or main in "eE":
            break
        else:
            print("\nPlease enter a valid choice...\n")
    except:
        continue



# FOR CUSTOMERS

if main in "cC":

    while True:

        print()
        print("\n\tPlease choose the operation:\n")
        print()
        print("1. Show Products")
        print("2. Search for products")
        print("3. Buy product(s)")
        print("4. Quit")
        print()


        while True:   # To avoid program crash due to typos

            try:
                choice = str(input("Enter the choice number: "))
        
                if choice == "1" or choice == "2" or choice == "3" or choice == "4":
                    break
                else:
                    print("\nPlease enter a valid choice...\n")
            except:
                continue

        
        print()
#Show 
        if choice == "1":

            print("\n\t\t\t\t\t\t\t\t\t\t\t  ++=> Our Products <=++\n")

            cshow()

            

#Search 
        elif choice == "2":

            print("\n\t\t\t\t\t\t\t\t\t\t\t  ++=> Search for a product <=++\n")

            csearch()

            
#Buy
        elif choice == "3":

            print("\n\t\t\t\t\t\t\t\t\t\t\t\t   ++=> Buy a Product <=++\n")
                        
            cbill()

            
                
        elif choice == "4":

            print("\n\t\t\t\t\t\t\t\t\t\t\t\t  ++=> Thank You <=++\n")
            break
            

# FOR EMPLOYEES

elif main in "eE":

    while True:

        print()
        print("\n\tPlease choose the operation:\n")
        print()
        print("1. Add a new product")
        print("2. Search for a product")
        print("3. Update the details of a product")
        print("4. Delete a product")
        print("5. PROFIT / LOSS")
        print("6. Show Inventory")
        print("7. Quit")
        print()

        while True:   # To avoid program crash due to typos

            try:
                choice = str(input("Enter the choice number: "))
    
                if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5" or choice == "6" or choice == "7":
                    break
                else:
                    print("\nPlease enter a valid choice...\n")
            except:
                continue
        print()

# Add

        if choice == '1':

            print("\n\t\t\t\t\t\t\t\t\t\t\t\t  ++=> Add <=++\n")
                        
            add()

            

# Search

        elif choice == '2':
                        
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t  ++=> Search <=++\n")

            esearch()

            

# Update

        elif choice == '3':

            print("\n\t\t\t\t\t\t\t\t\t\t\t\t  ++=> Update <=++\n")
            update()

            

# Delete

        elif choice == '4':

            print("\n\t\t\t\t\t\t\t\t\t\t\t\t  ++=> Delete <=++\n")
            delete()

            

# Profit / Loss Calculator

        elif choice == '5':

            print("\n\t\t\t\t\t\t\t\t\t\t\t  ++=> Profit / Loss Calculator <=++\n")
            
            profitloss()

            

# Show Inventory

        elif choice == '6':

            print("\n\t\t\t\t\t\t\t\t\t\t\t\t  ++=> Inventory <=++\n")
            
            eshow()

        
        elif choice == "7":
        
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t  ++=> Thank You <=++\n")
            break
