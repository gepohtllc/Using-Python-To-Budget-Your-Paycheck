print("50/30/20 - Using Python To Budget Your Paycheck \n")

after_tax_income = float(input("Enter your after tax income: ")) #this variable takes the user's input and converts it into a float.

needs = int(after_tax_income * 0.5) #user input times 50%.
wants = int(after_tax_income * 0.3) #user input times 30%.
savings = int(after_tax_income * 0.2) #user input times 20%.

print("\n") #used as a seperator.

print("You should allocate " + str(needs) + " to your needs. \n")
print("You should allocate " + str(wants) + " to your wants. \n")
print("You should allocate " + str(savings) + " to your savings.")