import mysql.connector
from tabulate import tabulate

def profitloss():

	while True:

		mydb = mysql.connector.connect(host='localhost', user='root', password='12345', database='project')
		mycursor = mydb.cursor()
		
		print("\nYou can choose from the following options: \n")
		
		print("1: Profit / Loss for a particular item / type of item")
		print("2: Overall Profit / Loss")
		print("3: back\n")
		
		choice = int(input("Enter the choice number: \n"))

		if choice == 1:
			
			mycursor.execute("select * from products;")
			result = mycursor.fetchall()
			print(tabulate(result, headers=["Product_Number", "Category", "Brand_Name", "Seller_Name", "Cost_Price", "Sale_Price", "Date_of_Purchase", "Quantity", "Detail", "Sold", "Sales", "Sale_Price_VAT"], tablefmt="fancy_grid"))
			
			
			while True:
				
				print("\nYou'd like to view the P/L of: \n")
				
				print("\t1: a product via its Product Number")
				print("\t2: a product type by searching for a Category")
				print("\t3: a product type by searching for a Brand Name")
				print("\t4: a product type by searching for a its Seller Name")
				print("\t5: a product type by searching for a its Detail")
				print("\t6: back\n")
				
				ch = input("Enter your choice: ")
				print()
				
				if ch == "1":
					
					plist = []
			
					for k in result:
						plist.append(k[0])
				
					ch1 = int(input("Enter the product number of the item: "))
					
					if ch1 in plist:
						
						mycursor.execute("select * from products where product_number={};".format(ch1))
						result1 = mycursor.fetchall()
						
						print(tabulate(result1, headers=["Product_Number", "Category", "Brand_Name", "Seller_Name", "Cost_Price", "Sale_Price", "Date_of_Purchase", "Quantity", "Detail", "Sold", "Sales", "Sale_Price_VAT"], tablefmt="fancy_grid"))
						
						ch2 = str(input("Is this your desired product? [y] / [n]: "))
						
						if ch2 in "Yy":

							bpsum, spsum = 0.0, 0.0 # Cost Price Sum, Sale Price Sum
							total, sold = 0, 0
							
							sales = result1[0][10] # Product sales (in CUR)
							sold = result1[0][9]
							total += sold # Quantity of product sold
							bp = result1[0][4] # Cost Price of the product
							
							spsum += float(sales)
							bpsum += float(sold) * float(bp)
							
							porl = spsum - bpsum #Profit or Loss (Sale Price - Cost Price)
							
							if porl > 0:
								print("\n-> {} products sold with 'PROFIT' worth CUR {}\n".format(total, porl))
								
								
							elif porl < 0:
								print("\n-> {} products sold with 'LOSS' worth CUR {}\n".format(total, porl))
								
							else:
								print("\n-> 0 products sold")
							
						
						else:
							continue
						
					else:
						print("INVALID CHOICE")
						continue
				
				elif ch == "2":
					
					plist = []
			
					for k in result:
						plist.append(k[1])
				
					ch1 = str(input("Enter the Category: "))
					
					
					if ch1 in plist:
						
						mycursor.execute("select * from products where category='{}';".format(ch1))
						result1 = mycursor.fetchall()
						
						print(tabulate(result1, headers=["Product_Number", "Category", "Brand_Name", "Seller_Name", "Cost_Price", "Sale_Price", "Date_of_Purchase", "Quantity", "Detail", "Sold", "Sales", "Sale_Price_VAT"], tablefmt="fancy_grid"))
						
						ch2 = str(input("Is this your desired category? [y] / [n]: "))
						
						if ch2 in "Yy":
							
							bpsum, spsum = 0.0, 0.0 # Cost Price Sum, Sale Price Sum
							total, sold = 0, 0
							
							for k in result1:
								
								sales = k[10] # Product sales (in CUR)
								sold = k[9]
								total += sold # Quantity of product sold
								bp = k[4] # Cost Price of the product
								
								spsum += float(sales)
								bpsum += float(sold) * float(bp)
								
							porl = spsum - bpsum #Profit or Loss (Sale Price - Cost Price)
							
							if porl > 0:
								print("\n-> {} products sold with 'PROFIT' worth CUR {}\n".format(total, porl))
								
								
							elif porl < 0:
								print("\n-> {} products sold with 'LOSS' worth CUR {}\n".format(total, porl))
								
							else:
								print("\n-> 0 products sold")

						else:
							continue
						
					else:
						print("INVALID CHOICE")
						continue
				
				
				elif ch == "3":
					
					plist = []
			
					for k in result:
						plist.append(k[2])
				
					ch1 = str(input("Enter the Brand Name: "))
					
					if ch1 in plist:
						
						mycursor.execute("select * from products where Brand_Name='{}';".format(ch1))
						result1 = mycursor.fetchall()
						
						print(tabulate(result1, headers=["Product_Number", "Category", "Brand_Name", "Seller_Name", "Cost_Price", "Sale_Price", "Date_of_Purchase", "Quantity", "Detail", "Sold", "Sales", "Sale_Price_VAT"], tablefmt="fancy_grid"))
						
						ch2 = str(input("Is this your desired brand name? [y] / [n]: "))
						
						if ch2 in "Yy":
							
							bpsum, spsum = 0.0, 0.0 # Cost Price Sum, Sale Price Sum
							total, sold = 0, 0
							
							for k in result1:
								
								sales = k[10] # Product sales (in CUR)
								sold = k[9]
								total += sold # Quantity of product sold
								bp = k[4] # Cost Price of the product
								
								spsum += float(sales)
								bpsum += float(sold) * float(bp)
								
							porl = spsum - bpsum #Profit or Loss (Sale Price - Cost Price)
							
							if porl > 0:
								print("\n-> {} products sold with 'PROFIT' worth CUR {}\n".format(total, porl))
								
								
							elif porl < 0:
								print("\n-> {} products sold with 'LOSS' worth CUR {}\n".format(total, porl))
								
							else:
								print("\n-> 0 products sold")

						else:
							continue
						
					else:
						print("INVALID CHOICE")
						continue
					
				elif ch == "4":
					
					plist = []
			
					for k in result:
						plist.append(k[3])
				
					ch1 = str(input("Enter the Seller Name: "))
					
					
					if ch1 in plist:
						
						mycursor.execute("select * from products where seller_name='{}';".format(ch1))
						result1 = mycursor.fetchall()
						
						print(tabulate(result1, headers=["Product_Number", "Category", "Brand_Name", "Seller_Name", "Cost_Price", "Sale_Price", "Date_of_Purchase", "Quantity", "Detail", "Sold", "Sales", "Sale_Price_VAT"], tablefmt="fancy_grid"))
						
						ch2 = str(input("Is this your desired seller name? [y] / [n]: "))
						
						if ch2 in "Yy":
							
							bpsum, spsum = 0.0, 0.0 # Cost Price Sum, Sale Price Sum
							total, sold = 0, 0
							
							for k in result1:
								
								sales = k[10] # Product sales (in CUR)
								sold = k[9]
								total += sold # Quantity of product sold
								bp = k[4] # Cost Price of the product
								
								spsum += float(sales)
								bpsum += float(sold) * float(bp)
								
							porl = spsum - bpsum #Profit or Loss (Sale Price - Cost Price)
							
							if porl > 0:
								print("\n-> {} products sold with 'PROFIT' worth CUR {}\n".format(total, porl))
								
								
							elif porl < 0:
								print("\n-> {} products sold with 'LOSS' worth CUR {}\n".format(total, porl))
								
							else:
								print("\n-> 0 products sold")

						else:
							continue
						
					else:
						print("\nINVALID CHOICE")
						continue

				elif ch == "6":
                                        break
					
				
				elif ch == "5":
					
					plist = []
			
					for k in result:
						plist.append(k[8])

				
					ch1 = str(input("Enter the Detail: "))
					
					
					if ch1 in plist:
						
						mycursor.execute("select * from products where detail='{}';".format(ch1))
						result1 = mycursor.fetchall()
						
						print(tabulate(result1, headers=["Product_Number", "Category", "Brand_Name", "Seller_Name", "Cost_Price", "Sale_Price", "Date_of_Purchase", "Quantity", "Detail", "Sold", "Sales", "Sale_Price_VAT"], tablefmt="fancy_grid"))
						
						ch2 = str(input("Is this your desired detail? [y] / [n]: "))
						
						if ch2 in "Yy":
							
							bpsum, spsum = 0.0, 0.0 # Cost Price Sum, Sale Price Sum
							total, sold = 0, 0
							
							for k in result1:
								
								sales = k[10] # Product sales (in CUR)
								sold = k[9]
								total += sold # Quantity of product sold
								bp = k[4] # Cost Price of the product
								
								spsum += float(sales)
								bpsum += float(sold) * float(bp)
								
							porl = spsum - bpsum #Profit or Loss (Sale Price - Cost Price)
							
							if porl > 0:
								print("\n-> {} products sold with 'PROFIT' worth CUR {}\n".format(total, porl))
								
								
							elif porl < 0:
								print("\n-> {} products sold with 'LOSS' worth CUR {}\n".format(total, porl))
								
							else:
								print("\n-> 0 products sold")

						else:
							continue
						
					else:
						print("\nINVALID CHOICE")
						continue
				
					
					
		elif choice == 2:
						
			bpsum, spsum = 0.0, 0.0 # Cost Price Sum, Sale Price Sum
			total, sold = 0, 0
			
			mycursor.execute("select * from products where Sold not in (0);")
			result = mycursor.fetchall()
			
			for k in result:

				sales = k[10] # Product sales (in CUR)
				sold = k[9]
				total += sold # Quantity of product sold
				bp = k[4] # Cost Price of the product
				
				spsum += float(sales)
				bpsum += float(sold) * float(bp)
				
			porl = spsum - bpsum #Profit or Loss (Sale Price - Cost Price)

			if porl > 0:
				print("\n-> {} products sold with 'PROFIT' worth CUR {}".format(total, porl))
				continue
				
			elif porl < 0:
				print("\n-> {} products sold with 'LOSS' worth CUR {}".format(total, porl))
				continue
			else:
				print("\n-> 0 products sold")

		elif choice == 3:
			break
