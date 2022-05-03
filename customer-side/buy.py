import mysql.connector
from tabulate import tabulate
import random

mydb=mysql.connector.connect(host='localhost',user='root',password='12345', database="project")
mycursor=mydb.cursor()

def cbill():

	print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t* BUY MENU *\n")

	mycursor.execute("select Product_Number, Category, Brand_Name, Sale_Price_VAT, Quantity, Detail from products")
	result = mycursor.fetchall()
	
	# Variables
	  
	allgood = True 
	cart = []
	total = 0.0
	price = 0.0
	sales = 0.0
	

	while allgood:  # Main Loop
		ok = True
		if allgood == False: # Condition to stop looping
			break

		discount = random.randint(0, 20) # For Discounts between 0% and 5%

		# Products Table which shows only the required columns

		mycursor.execute("select Product_Number, Category, Brand_Name, Sale_Price_VAT, Quantity, Detail from products")
		result = mycursor.fetchall()

		print(tabulate(result, headers=["Product_Number", "Category", "Brand_Name", "Price", "Quantity", "Detail"], tablefmt="fancy_grid"))
		print()

		pnolist = [] # List of all the product numbers
		
		for k in result:
			pnolist.append(k[0])

		while True:   # To avoid program crash due to typos

			try:
				pno = int(input("\nEnter the product number: ")) # Product number
				
				if pno in pnolist: # Proceed only if product number exists
					break
				else:
					print("\nPlease enter a valid product number...\n")
			except:
				print("\nPlease enter a valid product number...\n")
				continue
		print()

		# To display the details of the product selected by the customer

		mycursor.execute("select Product_Number, Category, Brand_Name, Sale_Price_VAT, Quantity, Detail from products where Product_Number={}".format(pno))
		result1 = mycursor.fetchall()

		print(tabulate(result1, headers=["Product_Number", "Category", "Brand_Name", "Price", "Quantity", "Detail"], tablefmt="fancy_grid"))

		if discount == 0:
			pass
		else:

			print("\n\t\tGood News, today we have a {}% discount on this item!".format(round(discount, 2))) # Display this msg only if discount != 0
			p = result1[0][3] # The price of the product mentioned
			new_price = round(float(p) - float((discount*p/100)), 2)
			print("\n\t\t\t\tNew Price: {}".format(new_price)) # New price (after subtracting the discount amount)
		print()

		while True: # To avoid program crash due to typos
			try:
				confirm = str(input("Is this your desired product? [y] / [n]: "))
				if confirm in "yY" or confirm in "nN":
					break
				else:
					continue
			except:
				continue

		mycursor.execute("select Category, Brand_Name, Quantity, Detail, Sale_Price_VAT from products where Product_Number={}".format(pno))
		qtyres = mycursor.fetchall()


		if confirm in "Yy":

			while True: # Nested while loop

				if allgood == False:
					break

				print()

				while True: # To avoid program crash due to typos
					if ok == False:
						break
							
					qty = int(input("Enter the quantity: "))
			
					qtyproduct = qtyres[0][2]
								
					if qty <= qtyproduct:
					
						cat = qtyres[0][0]
						bname = qtyres[0][1]
						det = qtyres[0][3]
						price = qtyres[0][4]
						total += (float(price) * float(qty)) - float(discount*price/100) # The total price shown at the time of checkout
						# discounted_price = float(price) * float(qty) - float(discount*price/100) # Discounted Price
						sales = float(float(price) - (10/100*float(price))) * float(qty) - float(discount*price/100) # For adding the details in database
						temp = [pno, bname, det, qty, new_price, new_price*qty] # For a fancier display of the cart
						ok = False
						break
							
					else:
						for k in result1:
							qty1 = k[4]
							print("\nSorry, we have only '{}' pieces in stock\n".format(int(qty1)))
							continue
														
			

				cart.append(temp) # Cart

				mycursor.execute("update products set Sales = Sales + {} where Product_Number={}".format(sales, pno))
				mycursor.execute("update products set Quantity = Quantity - {} where Product_Number={}".format(qty, pno))
				print("\nPRODUCT ADDED TO CART\n")

				while True: # To avoid program crash due to typos
					try:
						ch = str(input("Do you wish to continue shopping? [y] / [n]: "))
						if ch in "yY" or ch in "nN":
							break
						else:
							continue
					except:
						continue

				if ch in "Yy":
					break

				elif ch in "nN":

					print()
					while True: # To avoid program crash due to typos
						try:
							checkout = str(input("\nDo you wish to proceed for checkout? [y] / [n]: "))
							if checkout in "yY" or checkout in "nN":
								break
							else:
								continue
						except:
							continue

					if checkout in "yY":


						print()

						print("\n\t\t\t\tThis is your cart\n")

						print(tabulate(cart, headers=["Product Number", "Brand", "Detail", "Quantity", "Price", "Total Price"], tablefmt = "fancy_grid")) # Final cart
						print()
						print("\t\tCUR '{}' is your final amount".format(round(total, 2))) # Total amount
						print()

						while True: # To avoid program crash due to typos
							try:
								proceed = str(input("Do you wish to proceed? [y] / [n]: "))
								if proceed in "yY" or proceed in "nN":
									break
								else:
									continue
							except:
								continue

						if proceed in "nN":
							print("\nYour order will be cancelled\n")
							
							c = str(input("Are you sure? [y] / [n]: "))
							
							if c in "Yy":
								print("\nYour order has been cancelled!")
								print()
								allgood = False
								break
								
							elif c in "nN":
								break

						elif proceed in "Yy":
							mycursor.execute("update products set Sold = Sold + {} where Product_Number={}".format(qty, pno))

							while True: # To avoid program crash due to typos
								try:
									final = str(input("\nLAST ALERT: PLEASE CONFIRM THAT YOU'RE SURE ABOUT YOUR ORDER? [y] / [n]: ")) # The final ALERT
									if final in "yY" or final in "nN":
										break
									else:
										continue
								except:
									continue



							if final in "yY":
								mydb.commit()
								print("\nYOUR ORDER HAS BEEN MADE!\n")

								allgood = False
								break
								
							else:
								print("\nYour order has been cancelled!\n")
								allgood = False
								break


					elif checkout in "nN":

						while True: # To avoid program crash due to typos
							try:
								ask = str(input("Do you wish to continue shopping? [y] / [n]: "))
								if ask in "yY" or ask in "nN":
									break
								else:
									continue
							except:
								continue



						if ask in "Yy":
							break
						elif ask in "nN":
							allgood = False
							break


		elif confirm in "nN": # If the customer changes their mind once they see their desired product
			

			while True: # To avoid program crash due to typos
				try:
					choice = str(input("\nDo you wish to continue shopping? [y] / [n]: "))
					if choice in "yY" or choice in "nN":
						break
					else:
						continue
				except:
					continue

			if choice in "Yy":
				continue
			else:
				break
