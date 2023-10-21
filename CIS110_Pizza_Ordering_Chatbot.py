#Greeting
print("Hello, my name is ALex your virtual assistant. I will help you order a pizza!")
print("I am going to ask you a few questions. After typing an answer, press enter.")

#Ask user to input their name and store it in a variable
userName = input("\nEnter your name: ")

#Output a welcome sentence using the name stored in the variable
print(f"\nHello, {userName}. Nice to meet you!")

#Inputs needed from the user
size = input("\nWhat size would you like? Enter small, medium, or large:  ")
flavor = input("\nWhat kind of flavor would you like?:  ")
crustType = input("\nWhat type of crust would you like?:  ")
quantity = input("\nHow many of those would you like to order? Enter a numeric value:  ")
#Convert the characters the user typed in a interger
quantity = int(quantity)
method = input("\nIs this for delivery or carry out?:  ")

#Assign a fixed vaule for sales tax and price per pizza
salesTax = 1.1
pizzaCost = 14.99

#Algorithm to calculate the total cost of order
total = (pizzaCost * quantity) * salesTax

#Output order summary
print("-" * 10)
print(f"Thank you, {userName}, for you order.")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crustType} crust ${total:,.2f}.")
print("-" * 10)