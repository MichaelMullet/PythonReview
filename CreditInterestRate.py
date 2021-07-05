balance = 5000
annualInterestRate = 0.2

newBalance = balance
monthIntRate = (annualInterestRate) / 12.0
epsilon = 0.01
low = newBalance / 12.0
high = (newBalance * (1 + monthIntRate)**12) / 12.0
monthlyPayment = (high + low) / 2.0

while abs(high - low) >= epsilon:
    for month in range(12):
        newBalance -= monthlyPayment
        newBalance += monthIntRate * newBalance
    if newBalance > 0:
        month = 0
        newBalance = balance
        low = monthlyPayment
    else:
        month = 0
        newBalance = balance
        high = monthlyPayment
        
print('Lowest Payment: ' + str(round(monthlyPayment, 2))) 