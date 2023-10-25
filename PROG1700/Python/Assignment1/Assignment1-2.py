print("Weekly Loan Calculator")

    
loanMount = float(input("Enter the amount of loan: "))

interestRate = float(input("Enter the interest rate: "))

yearOfloan = float(input("Enter the number of year: "))

weeklyInterestRate = interestRate/5200
weeeklyPayment = (weeklyInterestRate /(1-(1 + weeklyInterestRate)**(-52*yearOfloan)) )* loanMount
 
print(f"Your weekly payment will be : ${round(weeeklyPayment,2)}")

