import matplotlib.pyplot as plt

loanInitAmount = 50000
yearlyPayment = 8000
interestFactor = 1.065
years = 100
loanAmounts = [loanInitAmount]
totalInterest = 0

for i in range(1, years):
    # if i == 1 or i == 2:
    #     yearlyPayment = yearlyPayment + 12000
    # yearlyPayment = 500 + loanAmounts[i-1] * 0.3
    loanAmounts.append(((loanAmounts[i-1] * interestFactor) - yearlyPayment))
    totalInterest += (loanAmounts[i-1] * interestFactor) - loanAmounts[i-1]
    # if i == 1 or i ==2:
    #     yearlyPayment = yearlyPayment - 12000
    if (loanAmounts[i-1] * interestFactor) - yearlyPayment < 0: break

plt.plot(loanAmounts)
plt.axhline(y=0, color='b', linestyle='-')
plt.title("Loan amount with: " + str(loanInitAmount) + " starting loan at an interest rate of " + str((100 * ( interestFactor - 1))) + " and a yearly payment of " + str(yearlyPayment))


for i in range(len(loanAmounts)):
    print(str(i) + ", " + str(loanAmounts[i]))

print("total paid: " + str(totalInterest + loanInitAmount))
print("total interest paid: " + str(totalInterest))

plt.show()