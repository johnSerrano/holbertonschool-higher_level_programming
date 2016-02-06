"""This program calculates
the amount you should pay
including tip and tax"""

#welcome line
print("Welcome to the taxes and tip calculator!")
#price input and prompt
price = float(input("What is the price before tax? "))
#tax input and prompt
tax = float(input("What are the taxes? (in %) "))
#tip input and prompt
tip = float(input("What do you want to tip? (in %) "))
#calculate price and print
print("the price you need to pay is " + str(((price*tax/100) + ((price*tax/100 + price)*tip/100) + price)) + ".")
