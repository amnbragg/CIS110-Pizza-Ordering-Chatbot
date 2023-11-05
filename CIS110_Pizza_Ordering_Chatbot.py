#Greeting
print("Hello, my name is Alex your virtual assistant. I will help you order a pizza!")
print("I am going to ask you a few questions. After typing an answer, press enter.")

#Ask user to input their name and store it in a variable
userName = input("\nEnter your name: ")
while len(userName) == 0:
    userName = input("Name cannot be blank! Please enter your name:  ")
    
#Output a welcome sentence using the name stored in the variable
if userName.lower() == "david bragg":
    print(f"\nMy creator, {userName}. Pleasure to serve you!")
else:
    print(f"\nHello, {userName}. Nice to meet you!")

#Inputs needed from the user
size = input("\nWhat size would you like? Enter small, medium, or large:  ")
while size.lower() not in ["small", "medium", "large" ]:
    size = input("Invalid vaule!  Please enter small, medium, or large:  ")
    
flavor = input("\nWhat kind of flavor would you like?:  ")
while len(flavor) == 0:
    flavor = input("Flavor cannot be blank!  Please enter a flavor:  ")
    
crustType = input("\nWhat type of crust would you like?:  ")
while len(crustType) == 0:
    crustType = input("Crust type cannot be blank!  Please enter crust type:  ")
    
quantity = input("\nHow many of those would you like to order? Enter a numeric value:  ")
while not quantity.isdigit():
    quanitiy = input("Vaule not recognized. Please enter a numeric vaule:  ")
quantity = int(quantity)

method = input("\nIs this for delivery or carry out?:  ")

#Set Delivery Fee
if method.lower() == "delivery":
    deliveryFee = 5
else:
    deliveryFee = 0

#Assign a fixed vaule for sales tax and price per pizza
salesTax = 1.1

#Set the price per pizza
if size.lower() == "small":
    pizzaCost = 8.99
elif size.lower() == "medium":
    pizzaCost = 14.99
elif size.lower() == "large":
    pizzaCost = 17.99

#Algorithm to calculate the total cost of order
total = (pizzaCost * quantity) * salesTax + deliveryFee

#Output order summary
print("-" * 10)
print(f"Thank you, {userName}, for you order.")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crustType} crust ${total:,.2f}.")
print("-" * 10)
print(f"Your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs${total:,.2f}.")

#Display Coupon if total price of order is greater than or equal to $50
if total >= 50:
    print("\nCongratulations! You've been awarded a $10 off coupon for your next order.")
else:
    print("\nOrder over $50 will receive a free $10 off coupon!")
    
print("-" * 10)