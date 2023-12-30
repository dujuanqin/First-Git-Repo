print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll pay on a home loan")
user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

#if elif else structure,
if user_input.lower() == "investment":
    p = int(input("How much do you want to deposit (£)? "))
    r = int(input("What is the annual interest rate that you desire (%)? "))
    t = int(input("How many years do you want to invest your money? "))
    interest = input("Simple or compound interest? ")
    #nested branching, interest type
    if interest.lower() == "simple":
        payback_simple = p * (1 + r * t)
        print(f"You will get {payback_simple} back after {t} years at the the interest rate of {r}%.")
    elif interest.lower()  == "compound":
        payback_compound = p * (1 + r)** t
        print(f"You will get {payback_compound} back after {t} years at the the interest rate of {r}%.")
    else:
        print("Error.")   
elif user_input.lower() == "bond":
    pv_house = int(input("Please enter the present value of the house(£): "))
    r_bond = int(input("Please enter the interest rate (%): "))
    t_bond = int(input("How many months do you plan to repay the bond? "))
    repayment = (r_bond/(100*12) * pv_house)/(1 - (1 + r_bond/(100*12))** (- t_bond ))
    print(f"You need to repay £{repayment} monthly.")
else:
    print("Error.")

