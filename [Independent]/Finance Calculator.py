# Jonathan Klein
# 11/7/18
# Finance Calculator.py

def line():
	print("="*50)

cost = 0.0
discount = 0.0
tax = 0.0
total = 0.0

running = True
master = True

while master:
	selection = input("What would you like to calculate? Type 'quit' to end program.\n 1. Sales Tax\n 2. Discount\n 3. Tip\n")
	running = True
	if selection == "1" or selection == "Sales Tax":
		while running:
			cost = float(input("What is your subtotal?\n"))
			tax = float(input("\nWhat is your state's sales tax? (Enter a percent)\n"))
			if cost > 10000000 or tax > 100 or tax <= 0:
				print("Invalid input. Please try again.\n")
			else:
				addedTax = cost*(tax/100)
				total = addedTax+cost
				print(f"\nThe added sales tax is ${round(addedTax, 2)}")
				print(f"Your total is ${round(total, 2)}")
				line()
				running = False
	elif selection == "2" or selection == "Discount":
		while running:
			cost = float(input("What is your subtotal?\n"))
			discount = float(input("What is the discount applied? (Enter a percent)\n"))
			if cost > 10000000 or discount <= 0:
				print("Invalid input. Please try again.\n")
			elif discount > 1:
				total = cost-((discount/100)*cost)
				print(f"\nYour total is ${round(total, 2)}")
				line()
				running = False
			elif discount > 0 and discount < 1:
				total = cost-(discount*cost)
				print(f"\nYour total is ${round(total, 2)}")
				line()
				running = False
	elif selection == "3" or selection == "Tip":
		while running:
			cost = float(input("What is your subtotal?\n"))
			percentTip = float(input("What would you like to tip? (Enter a percent)\n"))
			if percentTip > 1 and percentTip < 100:
				tip = round(((percentTip)/100)*cost, 2)
				print(f"Your tipped ${tip}, bringing your total to ${round((cost + tip), 2)}")
				line()
				running = False
			elif percentTip > 0 and percentTip < 1:
				tip = round(percentTip*cost, 2)
				print(f"Your tipped ${tip}, bringing your total to ${round((cost + tip), 2)}")
				line()
				running = False
			else:
				print("Invalid input. Please try again.\n")
	elif selection == "Quit" or selection == "quit":
		print("\nTake Care :)")
		master = False
	else:
		print("Invalid input. Please try again.\n")

