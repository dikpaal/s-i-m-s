import mysql.connector

def add():

	mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345",database="project")
	mycursor = mydb.cursor()
	
	mycursor.execute("select * from products;")
	result = mycursor.fetchall()
	
	pno = result[len(result) - 1][0]

	Product_Number = pno + 1
	Category = str(input("Enter the category of the product: "))
	Brand_Name = str(input("Enter the brand name: "))
	Seller_Name = str(input("Enter the seller name: "))
	Cost_Price = float(input("Enter the cost price: "))
	Sale_price = float(input("Enter the sale price: "))
	Date_of_Purchase = str(input("Enter the date of purchase: "))
	Quantity = int(input("Enter the quantity: "))
	Detail = str(input("Enter the detail of the product: "))
	Sold = 0
	Sales = 0
	Sale_Price_VAT = (10 * Sale_price/100) + Sale_price

	rec = (Product_Number, Category, Brand_Name, Seller_Name, Cost_Price, Sale_price, Date_of_Purchase, Quantity, Detail, Sold, Sales, Sale_Price_VAT)

	query = "insert into products(Product_Number, Category, Brand_Name, Seller_Name, Cost_Price, Sale_price, Date_of_Purchase, Quantity, Detail, Sold, Sales, Sale_Price_VAT) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	mycursor.execute(query, rec)
	mydb.commit()
	print("\nProduct Successfully added!")
