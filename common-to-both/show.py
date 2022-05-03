import mysql.connector
from tabulate import tabulate

def cshow():

	mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345",database="project" )
	mycursor = mydb.cursor()
	mycursor.execute("select Product_Number, Category, Brand_Name, Sale_Price_VAT, Quantity, Detail from products;")
	result = mycursor.fetchall()
	print(tabulate(result, headers=["Product_Number", "Category", "Brand_Name", "Price", "Quantity", "Detail"], tablefmt="fancy_grid"))



def eshow():

	mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345",database="project" )
	mycursor = mydb.cursor()
	mycursor.execute("select * from products;")
	result = mycursor.fetchall()
	print(tabulate(result, headers=["Product_Number", "Category", "Brand_Name", "Seller_Name", "Cost_Price", "Sale_Price", "Date_of_Purchase", "Quantity", "Detail", "Sold", "Sales", "Sale_Price_VAT"], tablefmt="fancy_grid"))
