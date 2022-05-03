import mysql.connector
from tabulate import tabulate



def csearch():

	while True:
		mydb = mysql.connector.connect(host="localhost",user="root",passwd="12345", database="project")

		print("1. Product Number")
		print("2. Category")
		print("3. Brand Name")
		print("4. Detail")
		print("5. back")
		print()
		ch = str(input("You'd like to search by: "))
		print()

		if ch == '1':
												
			Productno = int(input("Enter the product number: "))
			mycursor = mydb.cursor()
				
			mycursor.execute("select Product_Number, Category, Brand_Name, Sale_Price_VAT, Quantity, Detail from products where Product_Number={}".format(Productno))
			result = mycursor.fetchall()

			print(tabulate(result, headers=["Product_Number", "Category", "Brand_Name", "Price", "Quantity", "Detail"], tablefmt="fancy_grid"))
			break


		elif ch == '2':

			name = input("Enter the category of the product: ")
			mycursor = mydb.cursor()
			
			mycursor.execute("select Product_Number, Category, Brand_Name, Sale_Price_VAT, Quantity, Detail from products where Category='{}'".format(name))
			result = mycursor.fetchall()

			print(tabulate(result, headers=["Product_Number", "Category", "Brand_Name", "Price", "Quantity", "Detail"], tablefmt="fancy_grid"))
			break

			

		elif ch == '3':   

			brand = input("Enter the name of the brand: ")
			mycursor = mydb.cursor()
 
			mycursor.execute("select Product_Number, Category, Brand_Name, Sale_Price_VAT, Quantity, Detail from products where Brand_Name='{}'".format(brand))
			result = mycursor.fetchall()

			print(tabulate(result, headers=["Product_Number", "Category", "Brand_Name", "Price", "Quantity", "Detail"], tablefmt="fancy_grid"))
			break

			
		elif ch == '4':

			detail = input("Enter the detail of the product: ")
			mycursor = mydb.cursor()

			mycursor.execute("select Product_Number, Category, Brand_Name, Sale_Price_VAT, Quantity, Detail from products where Detail='{}'".format(detail))
			result = mycursor.fetchall()

			print(tabulate(result, headers=["Product_Number", "Category", "Brand_Name", "Price", "Quantity", "Detail"], tablefmt="fancy_grid"))
			break
			
		elif ch == '5':
			break
			
		else:
			print("\nINVALID RESPONSE")


def esearch():

	while True:
		mydb = mysql.connector.connect(host="localhost",user="root",passwd="12345", database="project")

		print("1. Product Number")
		print("2. Category")
		print("3. Brand Name")
		print("4. Detail")
		print("5. back")
		print()
		ch = str(input("You'd like to search by: "))
		print()

		if ch == '1':
	 
			Productno = int(input("Enter the product number: "))
			mycursor = mydb.cursor()
   
			mycursor.execute("select * from products where Product_Number={}".format(Productno))
			result = mycursor.fetchall()

			print(tabulate(result, headers=["Product_Number", "Category", "Brand_Name", "Seller_Name", "Cost_Price", "Sale_Price", "Date_of_Purchase", "Quantity", "Detail", "Sold", "Sales", "Sale_Price_VAT"], tablefmt="fancy_grid"))
			break


		elif ch == '2':

			name = input("Enter the catgory of the product: ")
			mycursor = mydb.cursor()
			
			mycursor.execute("select * from products where category='{}'".format(name))
			result = mycursor.fetchall()
	 
			print(tabulate(result, headers=["Product_Number", "Category", "Brand_Name", "Seller_Name", "Cost_Price", "Sale_Price", "Date_of_Purchase", "Quantity", "Detail", "Sold", "Sales", "Sale_Price_VAT"], tablefmt="fancy_grid"))
			break

			

		elif ch == '3':   

			brand = input("Enter the name of the brand: ")
			mycursor = mydb.cursor()
 
			mycursor.execute("select * from products where Brand_Name='{}'".format(brand))
			result = mycursor.fetchall()

			print(tabulate(result, headers=["Product_Number", "Category", "Brand_Name", "Seller_Name", "Cost_Price", "Sale_Price", "Date_of_Purchase", "Quantity", "Detail", "Sold", "Sales", "Sales_with_VAT"], tablefmt="fancy_grid"))
			break

			
		elif ch == '4':

			detail = input("Enter the detail of the product: ")
			mycursor = mydb.cursor()

			mycursor.execute("select * from products where Detail='{}'".format(detail))
			result = mycursor.fetchall()

			print(tabulate(result, headers=["Product_Number", "Category", "Brand_Name", "Seller_Name", "Cost_Price", "Sale_Price", "Date_of_Purchase", "Quantity", "Detail", "Sold", "Sales", "Sale_Price_VAT"], tablefmt="fancy_grid"))
			break
		
		elif ch == "5":
			break
			
		else:
			print("\nINVALID RESPONSE")
