import math

# Ask the user to choose between investment and bond. 
user_input = input("\nOptions:\n1: Investment - to calculate the amount of interest you'll earn on your investment\n2: Bond - to calculate the amount you'll pay on a home loan\n\nEnter either 'Investment' or 'Bond' to proceed: ")

# Ask the user to enter different parameters based on the user's choice above.
if user_input.lower() == "investment": # Request input of investment calculator parameters
    deposit_amount = int(input("How much do you want to deposit (£)? "))
    interest_rate = int(input("What is the annual interest rate that you desire (%)? "))
    time = int(input("How many years do you want to invest your money? "))
    interest = input("Simple or compound interest? ")

    # Calculate investment payback under simple or compound interest using different formulas.
    if interest.lower() == "simple": 
        payback_simple = round(deposit_amount * (1 + interest_rate /100 * time), 2)
        print(f"You will get £{payback_simple} back after {time} year(s) with an interest rate of {interest_rate}%.")
    elif interest.lower()  == "compound":
        payback_compound = round(deposit_amount * math.pow((1 + interest_rate/100),time),2)
        print(f"You will get £{payback_compound} back after {time} year(s) with an interest rate of {interest_rate}%.")
    else:
        print("Invalid input. Please try again.")   

elif user_input.lower() == "bond": # Request input of home loan repayment calculator parameters
    house_value = int(input("Please enter the present value of the house(£): "))
    interest_rate_bond = int(input("Please enter the interest rate (%): "))
    time_bond = int(input("How many months do you plan to repay the bond? "))
    repayment = round((interest_rate_bond/(100*12) * house_value)/(1 - (1 + interest_rate_bond/(100*12))** (- time_bond )),2)
    print(f"You will need to repay £{repayment} monthly.")

else: # Error message
    print("Invalid input. Please try again.")

