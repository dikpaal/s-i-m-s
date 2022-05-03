import mysql.connector
from tabulate import tabulate

def delete():

	mydb = mysql.connector.connect(host="localhost",user="root",passwd="12345",database="project")
	mycursor = mydb.cursor()
	mycursor.execute("select * from products;")
	result = mycursor.fetchall()
	
	print(tabulate(result, headers=["Product_Number", "Category", "Brand_Name", "Seller_Name", "Cost_Price", "Sale_Price", "Date_of_Purchase", "Quantity", "Detail", "Sold", "Sales", "Sale_Price_VAT"], tablefmt="fancy_grid"))

	Product_Number = int(input("Enter the product number: "))
	mycursor.execute("select * from products where Product_Number={};".format(Product_Number))
	result = mycursor.fetchall()

	print(tabulate(result, headers=["Product_Number", "Category", "Brand_Name", "Seller_Name", "Cost_Price", "Sale_Price", "Date_of_Purchase", "Quantity", "Detail", "Sold", "Sales", "Sale_Price_VAT"], tablefmt="fancy_grid"))

	while True:

		print()
		confirmation = str(input("ARE YOU SURE YOU WANT TO DELETE THIS PRODUCT? [y] / [n]: "))

		if confirmation in "Yy":
			query = "delete from products where Product_Number={};".format(Product_Number)
			mycursor.execute(query)
			mydb.commit()
			print("\nProduct Deleted Successfully!")
			break
		elif confirmation in "Nn":
			break
		else:
			continue
