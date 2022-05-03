import mysql.connector
from tabulate import tabulate

mydb=mysql.connector.connect(host='localhost',user='root',password='12345', database="project")
mycursor=mydb.cursor()

def update():

	pnolst = []
	mycursor.execute("select * from products;")
	result = mycursor.fetchall()

	for k in result:
		pnolst.append(k[0])
	
	print(tabulate(result, headers=["Product_Number", "Category", "Brand_Name", "Seller_Name", "Cost_Price", "Sale_Price", "Date_of_Purchase", "Quantity", "Detail", "Sold", "Sales", "Sales_with_VAT"], tablefmt="fancy_grid"))


	pno=int(input("Enter the product number to be updated: "))
	
	mycursor.execute("select * from products where Product_Number={};".format(pno))
	result=mycursor.fetchall()
	print(tabulate(result, headers=["Product_Number", "Category", "Brand_Name", "Seller_Name", "Cost_Price", "Sale_Price", "Date_of_Purchase", "Quantity", "Detail", "Sold", "Sales", "Sales_with_VAT"], tablefmt="fancy_grid"))

	while True:

		print("You can update the following:")
		print()
		print("1: Category")
		print("2: Brand Name")
		print("3: Seller Name")
		print("4: Cost Price")
		print("5: Sale Price")
		print("6: Date of Purchase")
		print("7: Quantity")
		print("8: Detail")
		print("9: Sold")
		print("10: Sales")
		print("11: Sale_Price_VAT")
		print("12. back")
		print()

	
		ch=int(input("Enter your operation number: "))

	
		if ch==1:
			upcategory=input("\nEnter the new category: ")
			ch2 = str(input("\nARE YOU SURE THAT YOU WANT TO UPDATE? [y] / [n]: "))

			if ch2 in "Yy":

				mycursor.execute("update products set Category='{}' where Product_Number={};".format(upcategory,pno))
				mydb.commit()
				print("\nThe data has been succesfully updated")
				break
			else:
				print("\n\n\t\t\t\t\t\t\t\t\t\t DATA NOT UPDATED \n")
				break


		elif ch==2:
			ubname=input("\nEnter the new Brand Name: ")
			ch2 = str(input("\nARE YOU SURE THAT YOU WANT TO UPDATE? [y] / [n]: "))

			if ch2 in "Yy":

				mycursor.execute("update products set Brand_Name='{}' where Product_Number={};".format(ubname,pno))
				mydb.commit()
				print("\nThe data has been succesfully updated")
				break
			else:
				print("\n\n\t\t\t\t\t\t\t\t\t\t DATA NOT UPDATED \n")
				break


		elif ch==3:
			usname=input("\nEnter the new Seller Name: ")
			ch2 = str(input("\nARE YOU SURE THAT YOU WANT TO UPDATE? [y] / [n]: "))

			if ch2 in "Yy":

				mycursor.execute("update products set Seller_Name='{}' where Product_Number={};".format(usname,pno))
				mydb.commit()
				print("\nThe data has been succesfully updated")
				break
			else:
				print("\n\n\t\t\t\t\t\t\t\t\t\t DATA NOT UPDATED \n")
				break

		elif ch==4:
			cprice=float(input("\nEnter the new Cost Price: "))
			ch2 = str(input("\nARE YOU SURE THAT YOU WANT TO UPDATE? [y] / [n]: "))

			if ch2 in "Yy":

				mycursor.execute("update products set Cost_Price={} where Product_Number={};".format(cprice,pno))
				mydb.commit()
				print("\nThe data has been succesfully updated")
				break
			else:
				print("\n\n\t\t\t\t\t\t\t\t\t\t DATA NOT UPDATED \n")
				break

		elif ch==5:
			sprice=float(input("\nEnter the new Sale Price: "))
			spv = sprice + (10 * sprice / 100)
			ch2 = str(input("\nARE YOU SURE THAT YOU WANT TO UPDATE? [y] / [n]: "))

			if ch2 in "Yy":

				mycursor.execute("update products set Sale_Price={} where Product_Number={};".format(sprice,pno))
				mycursor.execute("update products set Sale_Price_VAT={} where Product_Number={};".format(spv,pno))
				mydb.commit()
				print("\nThe data has been succesfully updated")
				break
			else:
				print("\n\n\t\t\t\t\t\t\t\t\t\t DATA NOT UPDATED \n")
				break

		elif ch==6:
			date=str(input("\nEnter the new Date of Purchase: "))
			ch2 = str(input("\nARE YOU SURE THAT YOU WANT TO UPDATE? [y] / [n]: "))

			if ch2 in "Yy":

				mycursor.execute("update products set Date_of_Purchase='{}' where Product_Number={};".format(date,pno))
				mydb.commit()
				print("\nThe data has been succesfully updated")
				break
			else:
				print("\n\n\t\t\t\t\t\t\t\t\t\t DATA NOT UPDATED \n")
				break

		elif ch==7:
			qty=int(input("\nEnter the new Quantity: "))
			ch2 = str(input("\nARE YOU SURE THAT YOU WANT TO UPDATE? [y] / [n]: "))

			if ch2 in "Yy":

				mycursor.execute("update products set Quantity={} where Product_Number={};".format(qty,pno))
				mydb.commit()
				print("\nThe data has been succesfully updated")
				break
			else:
				print("\n\n\t\t\t\t\t\t\t\t\t\t DATA NOT UPDATED \n")
				break

		elif ch==8:
			detail=str(input("\nEnter the new Detail: "))
			ch2 = str(input("\nARE YOU SURE THAT YOU WANT TO UPDATE? [y] / [n]: "))

			if ch2 in "Yy":

				mycursor.execute("update products set Detail='{}' where Product_Number={};".format(detail,pno))
				mydb.commit()
				print("\nThe data has been succesfully updated")
				break
			else:
				print("\n\n\t\t\t\t\t\t\t\t\t\t DATA NOT UPDATED \n")
				break
			
		elif ch==9:
			sold=int(input("\nEnter the new 'Sold items' number: "))
			ch2 = str(input("\nARE YOU SURE THAT YOU WANT TO UPDATE? [y] / [n]: "))

			if ch2 in "Yy":

				mycursor.execute("update products set Sold={} where Product_Number={};".format(sold,pno))
				mydb.commit()
				print("\nThe data has been succesfully updated")
				break
			else:
				print("\n\n\t\t\t\t\t\t\t\t\t\t DATA NOT UPDATED \n")
				break

		elif ch==10:
			sales=float(input("\nEnter the new sales: "))
			ch2 = str(input("\nARE YOU SURE THAT YOU WANT TO UPDATE? [y] / [n]: "))

			if ch2 in "Yy":

				mycursor.execute("update products set sales={} where Product_Number={};".format(sales,pno))
				mydb.commit()
				print("\nThe data has been succesfully updated")
				break
			else:
				print("\n\n\t\t\t\t\t\t\t\t\t\t DATA NOT UPDATED \n")
				break
				
		elif ch==11:
			sale_price_vat=float(input("\nEnter the new sale price with VAT: "))
			ch2 = str(input("\nARE YOU SURE THAT YOU WANT TO UPDATE? [y] / [n]: "))
			
			if ch2 in "Yy":

				mycursor.execute("update products set Sale_Price_VAT={} where Product_Number={};".format(sale_price_vat,pno))
				mydb.commit()
				print("\nThe data has been succesfully updated")
				break
			else:
				print("\n\n\t\t\t\t\t\t\t\t\t\t DATA NOT UPDATED \n")
				break
				
		elif ch==12:
			break
		
		else:
			print("\nINVALID RESPONSE")
